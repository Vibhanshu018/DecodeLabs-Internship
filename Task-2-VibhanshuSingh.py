# ============================================================
#  Data Classification Using AI — KNN on Iris Dataset
#  Author  : Vibhanshu
#  Batch   : 2026 | DecodeLabs Industrial Training
# ============================================================

# ---------- 1. IMPORTS ----------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    f1_score,
    accuracy_score,
)

print("=" * 60)
print("   PROJECT 2 : Data Classification Using KNN + Iris")
print("=" * 60)

# ---------- 2. LOAD & EXPLORE DATASET ----------
iris   = load_iris()
X      = iris.data                         # shape (150, 4)
y      = iris.target
labels = iris.target_names                 # setosa / versicolor / virginica

df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(y, labels)

print("\n[ Dataset Overview ]")
print(f"  Samples    : {X.shape[0]}")
print(f"  Features   : {X.shape[1]}")
print(f"  Classes    : {list(labels)}")
print("\n  First 5 rows:")
print(df.head().to_string(index=False))
print("\n  Class distribution:")
print(df["species"].value_counts().to_string())

# ---------- 3. FEATURE SCALING ----------
scaler   = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n[ Feature Scaling → StandardScaler ]")
print(f"  Mean (post-scale) : {X_scaled.mean(axis=0).round(4)}")
print(f"  Std  (post-scale) : {X_scaled.std(axis=0).round(4)}")

# ---------- 4. TRAIN-TEST SPLIT (80 / 20) ----------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.20, random_state=42, shuffle=True
)

print(f"\n[ Train-Test Split ]")
print(f"  Training samples : {len(X_train)}")
print(f"  Testing  samples : {len(X_test)}")

# ---------- 5. FIND OPTIMAL K (Elbow Method) ----------
error_rates = []
k_range     = range(1, 21)

for k in k_range:
    knn  = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(1 - accuracy_score(y_test, preds))

optimal_k = k_range[np.argmin(error_rates)]
print(f"\n[ Elbow Method → Optimal K = {optimal_k} ]")

# ---------- 6. TRAIN FINAL MODEL ----------
model = KNeighborsClassifier(n_neighbors=optimal_k)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ---------- 7. EVALUATION ----------
acc     = accuracy_score(y_test, y_pred)
f1_mac  = f1_score(y_test, y_pred, average="macro")
f1_wei  = f1_score(y_test, y_pred, average="weighted")
cm      = confusion_matrix(y_test, y_pred)

print("\n[ Model Performance ]")
print(f"  Accuracy       : {acc * 100:.2f}%")
print(f"  F1 (macro)     : {f1_mac:.4f}")
print(f"  F1 (weighted)  : {f1_wei:.4f}")
print("\n[ Classification Report ]")
print(classification_report(y_test, y_pred, target_names=labels))

# ---------- 8. VISUALISATIONS ----------
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Project 2 — KNN Iris Classification Results", fontsize=14, fontweight="bold")

# 8a — Elbow curve
ax = axes[0]
ax.plot(k_range, error_rates, marker="o", color="#1a3a5c", linewidth=2)
ax.scatter([optimal_k], [error_rates[optimal_k - 1]],
           color="#e8541e", s=120, zorder=5, label=f"Optimal K={optimal_k}")
ax.set_title("Elbow Method — Choosing K")
ax.set_xlabel("K Value")
ax.set_ylabel("Error Rate")
ax.legend()
ax.grid(alpha=0.3)

# 8b — Confusion matrix
ax = axes[1]
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=labels, yticklabels=labels, ax=ax,
            linewidths=0.5, cbar=False)
ax.set_title("Confusion Matrix")
ax.set_xlabel("Predicted Label")
ax.set_ylabel("True Label")

# 8c — F1 per class
ax = axes[2]
per_class_f1 = f1_score(y_test, y_pred, average=None)
bars = ax.bar(labels, per_class_f1, color=["#1a3a5c", "#e8541e", "#2e7d5e"],
              edgecolor="white", width=0.5)
for bar, val in zip(bars, per_class_f1):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.01, f"{val:.2f}", ha="center", fontsize=10)
ax.set_title("F1 Score per Class")
ax.set_ylabel("F1 Score")
ax.set_ylim(0, 1.15)
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/knn_results.png", dpi=150, bbox_inches="tight")
plt.close()
print("\n[ Plots saved → knn_results.png ]")

# ---------- 9. CUSTOM PREDICTION DEMO ----------
print("\n[ Custom Prediction Demo ]")
sample = np.array([[5.1, 3.5, 1.4, 0.2]])   # typical setosa
sample_scaled = scaler.transform(sample)
prediction    = model.predict(sample_scaled)
probabilities = model.predict_proba(sample_scaled)[0]

print(f"  Input features : {sample[0]}")
print(f"  Predicted class: {labels[prediction[0]]}")
print("  Class probabilities:")
for cls, prob in zip(labels, probabilities):
    print(f"    {cls:<12} : {prob:.2f}")

print("\n[ Done ] Model training & evaluation complete.")
