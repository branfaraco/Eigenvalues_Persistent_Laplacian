import os
import numpy as np
import pandas as pd
import petls

#  "config" inline
out_path = os.path.join(os.path.dirname(__file__), "dataset.parquet")

# general parameters
n_clouds = 50
n_points = 60
ambient_dim = 2
rng_seed = 0

max_dim = 2
threshold = 0.6

m_levels = 20
dim = 1
k_feat = 3
nonzero_tol = 1e-5



def pick_filt_values(K, m_levels):
    filts = np.asarray(K.get_all_filtrations(), dtype=float)
    if filts.size == 0:
        return np.array([], dtype=float)
    idx = np.linspace(0, filts.size - 1, m_levels).astype(int)
    return filts[idx]

def main():


    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    rng = np.random.default_rng(rng_seed)

    rows = []

    # for each point cloud
    for sample_id in range(n_clouds):
        X = rng.random((n_points, ambient_dim))
        K = petls.Rips(points=X, max_dim=max_dim, threshold=threshold)

        filt_values = pick_filt_values(K, m_levels)
        if filt_values.size < 2:
            continue

        for i in range(filt_values.size - 1):
            # Compute a,b
            a, b = float(filt_values[i]), float(filt_values[i + 1])

            eigs = np.asarray(K.spectra(dim=dim, a=a, b=b), dtype=float)   # source K_a  -> size = dim C_1^a
            nz = eigs[eigs > nonzero_tol]

            # dC1(a,b) = dim C_1^b - dim C_1^a ; dim C_1^b = size of the Hodge Laplacian of K_b (a=b)
            size_b = np.asarray(K.spectra(dim=dim, a=b, b=b), dtype=float).size
            dC1_edges_added = int(size_b - eigs.size)
                        
            row = {
                    "a": a,
                    "delta_ab": float(b - a),   
                    "dim": int(dim),
                    "sample_id": int(sample_id),
                    "num_eigs": int(eigs.size),
                    "dC1_edges_added": dC1_edges_added,
                    "nz_eig1": float(nz[0]) if nz.size > 0 else np.nan,
                    "nz_eig2": float(nz[1]) if nz.size > 1 else np.nan,
                    "nz_eig3": float(nz[2]) if nz.size > 2 else np.nan,
                }
                
            rows.append(row)

    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.sort_values(["sample_id", "a"]).reset_index(drop=True)

    df.to_parquet(out_path, index=False)
    print(f"Wrote {len(df)} rows to {out_path}")

if __name__ == "__main__":
    main()
