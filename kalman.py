import numpy as np
import matplotlib.pyplot as plt


class KalmanFilter:
    def __init__(self, F, H, Q, R, x0, P0):
        self.F = F # State transition matrix
        self.H = H # Observation matrix
        self.Q = Q # Process noise covariance matrix
        self.R = R # Observation noise covariance matrix
        self.x = x0 # Initial state vector
        self.P = P0 # Initial covariance matrix
    
    def predict(self):
        # Predict the next state
        self.x = np.dot(self.F, self.x)
        # Predict the next covariance matrix
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
    
    def update(self, z):
        # Calculate the Kalman gain
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(np.dot(np.dot(self.H, self.P), self.H.T) + self.R))
        # Update the state vector
        self.x = self.x + np.dot(K, z - np.dot(self.H, self.x))
        # Update the covariance matrix
        self.P = self.P - np.dot(np.dot(K, self.H), self.P)


# Generate some noisy measurements
np.random.seed(0)
N = 50
true_pos = 2*np.arange(N)
measured_pos = true_pos + 10*np.random.randn(N)

# Define the Kalman filter parameters
dt = 1.0  # Time step
F = np.array([[1, dt], [0, 1]])  # State transition matrix
H = np.array([[1, 0]])  # Observation matrix
Q = np.array([[1, 0], [0, 1]])  # Process noise covariance matrix
R = np.array([[100]])  # Observation noise covariance matrix
x0 = np.array([measured_pos[0], 0])  # Initial state vector
P0 = np.array([[100, 0], [0, 100]])  # Initial covariance matrix

# Create the Kalman filter object
kf = KalmanFilter(F, H, Q, R, x0, P0)

# Run the Kalman filter on the measurements
estimated_pos = []
for z in measured_pos:
    kf.predict()
    kf.update(z)
    estimated_pos.append(kf.x[0])

# Plot the true position, measured position, and estimated position
plt.plot(true_pos, label='True Position')
plt.plot(measured_pos, label='Measured Position')
plt.plot(estimated_pos, label='Estimated Position')
plt.legend()
plt.show()