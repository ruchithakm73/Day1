import numpy as np

np.random.seed(1)
scores = np.random.randint(50, 101, size=(5, 3))
print("Original Scores:")
print(scores)

mean_scores = scores.mean(axis=0)
print("\nMean of each subject:")
print(mean_scores)

centered_scores = scores - mean_scores
print("\nCentered Scores:")
print(centered_scores)


