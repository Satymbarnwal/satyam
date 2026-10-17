import numpy as np
from PIL import Image, ImageFilter

def runfill(seed, mask):
    """1D: any run of consecutive mask pixels containing a seed becomes all-seed."""
    starts = mask & ~np.concatenate([[False], mask[:-1]])
    gid = np.cumsum(starts) * mask
    hit = np.bincount(gid, weights=(seed & mask).astype(np.int64),
                      minlength=gid.max()+1) > 0
    hit[0] = False
    return mask & hit[gid]

def fill_rows(seed, mask):
    H, W = mask.shape
    z = np.zeros((H,1), bool)
    m = np.concatenate([mask, z], axis=1).ravel()
    s = np.concatenate([seed, z], axis=1).ravel()
    return runfill(s, m).reshape(H, W+1)[:, :W]

def flood(seed, mask):
    """True gap-respecting flood fill: alternate row and column run-fills."""
    for i in range(300):
        prev = seed.copy()
        seed = fill_rows(seed, mask) | seed
        seed = (fill_rows(seed.T.copy(), mask.T.copy()) | seed.T).T.copy()
        if np.array_equal(seed, prev):
            return seed, i+1
    return seed, 300

def erode(m,k):
    for _ in range(k):
        e=m.copy(); e[1:]&=m[:-1]; e[:-1]&=m[1:]; e[:,1:]&=m[:,:-1]; e[:,:-1]&=m[:,1:]; m=e
    return m
def dilate(m,k):
    for _ in range(k):
        d=m.copy(); d[1:]|=m[:-1]; d[:-1]|=m[1:]; d[:,1:]|=m[:,:-1]; d[:,:-1]|=m[:,1:]; m=d
    return m

src = Image.open('/home/user/satyam/satyam.webp').convert('RGB')
a = np.asarray(src).astype(np.int16); H, W, _ = a.shape
spread = a.max(axis=2) - a.min(axis=2); bright = a.mean(axis=2)
# background is neutral and mid-bright; skin has far too much chroma to qualify
bgmask = (spread < 26) & (bright > 140) & (bright < 234)

seed = np.zeros((H,W), bool)
seed[0] |= bgmask[0]; seed[:,0] |= bgmask[:,0]; seed[:,-1] |= bgmask[:,-1]
seed, n1 = flood(seed, bgmask)
print(f"flood A: {n1} passes, cut={100*seed.mean():.1f}%")

# kill thin leaks along the lapel, then re-check what is still border-reachable
seed = dilate(erode(seed, 3), 3) & bgmask
s2 = np.zeros((H,W), bool)
s2[0] |= seed[0]; s2[:,0] |= seed[:,0]; s2[:,-1] |= seed[:,-1]
s2, n2 = flood(s2, seed)
print(f"flood B: {n2} passes, islands dropped={seed.sum()-s2.sum()}px")
seed = s2

m = erode(~seed, 2)
al = Image.fromarray(np.where(m,255,0).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0))
out = src.convert('RGBA'); out.putalpha(al); out = out.crop(out.getbbox())
print("final size", out.size)
out.save('/home/user/satyam/satyam-cut.webp', quality=90, method=6)
flat = Image.new('RGB', out.size, (255,255,255)); flat.paste(out,(0,0),out)
flat.save('/home/user/satyam/satyam-white.webp', quality=90, method=6)
