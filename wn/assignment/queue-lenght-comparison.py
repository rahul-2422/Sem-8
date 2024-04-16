import numpy as np
import matplotlib.pyplot as plt


def calculate_queue_length(lambda_arrival, mu_service, t_max, num_points):
    """
    Calculate the queue lengths for M/D/1 and M/M/1 queuing systems.

    Parameters:
    lambda_arrival (float): Arrival rate
    mu_service (float): Service rate
    t_max (float): Maximum time
    num_points (int): Number of points to calculate

    Returns:
    t (np.ndarray): Time array
    Q_D (np.ndarray): Queue length for M/D/1 queue
    Q_M (np.ndarray): Queue length for M/M/1 queue
    """
    # Calculate the time step
    dt = t_max / (num_points - 1)

    # Initialize arrays for time and queue lengths
    t = np.linspace(0, t_max, num_points)
    Q_D = np.zeros_like(t)
    Q_M = np.zeros_like(t)

    # Calculate the queue lengths
    for i in range(1, num_points):
        # Calculate the utilization factor
        rho = lambda_arrival / mu_service

        # Update the queue lengths
        Q_D[i] = Q_D[i - 1] + dt * (
            lambda_arrival - mu_service * (1 - rho * np.heaviside(Q_D[i - 1], 0.5))
        )
        Q_M[i] = Q_M[i - 1] + dt * (
            lambda_arrival - mu_service * (1 - rho * np.exp(-Q_M[i - 1]))
        )

    return t, Q_D, Q_M


def print_comparrision_graph(flag, t, Q_D, Q_M, i):
    if flag == "invert":
        plt.figure(figsize=(8, 6))
        plt.plot(t, Q_D, label="M/D/1 Queue Length")
        plt.plot(t, Q_M, label="M/M/1 Queue Length")
        plt.gca().invert_yaxis()
        plt.xlabel("Time")
        plt.ylabel("Queue Length")
        plt.title(f"Comparison of M/D/1 and M/M/1 Queue Lengths (Scenario {i+1})")
        plt.legend()
        plt.show()
    else:
        plt.figure(figsize=(8, 6))
        plt.plot(t, Q_D, label="M/D/1 Queue Length")
        plt.plot(t, Q_M, label="M/M/1 Queue Length")
        plt.xlabel("Time")
        plt.ylabel("Queue Length")
        plt.title(f"Comparison of M/D/1 and M/M/1 Queue Lengths (Scenario {i+1})")
        plt.legend()
        plt.show()


def compare_queue_lengths(scenarios):
    """
    Compare the queue lengths for M/D/1 and M/M/1 queuing systems across different scenarios.

    Parameters:
    scenarios (list): List of tuples containing (lambda_arrival, mu_service, t_max, num_points)
    """
    for i, (lambda_arrival, mu_service, t_max, num_points) in enumerate(scenarios):

        t, Q_D, Q_M = calculate_queue_length(
            lambda_arrival, mu_service, t_max, num_points
        )

        # Calculate the mean queue lengths
        mean_Q_D = np.mean(Q_D)
        mean_Q_M = np.mean(Q_M)

        # Determine the queue with shorter length
        if mean_Q_D < mean_Q_M:
            print(
                f"Scenario {i+1}: M/D/1 queue has a shorter mean queue length than M/M/1 queue."
            )
            print_comparrision_graph("invert", t, Q_D, Q_M, i)
        else:
            print(
                f"Scenario {i+1}: M/M/1 queue has a shorter mean queue length than M/D/1 queue."
            )
            print_comparrision_graph("same", t, Q_D, Q_M, i)


# Define the scenarios
scenarios = [
    (0.5, 1.0, 100, 1000),  # Scenario 1
    (0.8, 1.0, 100, 1000),  # Scenario 2
    (0.5, 2.0, 100, 1000),  # Scenario 3
    (0.8, 2.0, 100, 1000),  # Scenario 4
    (0.2, 0.5, 100, 1000),  # Scenario 5
]

# print()

print(
    "The Scenarios are: (lambda_arrival, mu_service, t_max, num_points)\n"+
    "\n".join(
        f"Scenario-{i+1}: {scenario}"
        for i, scenario in enumerate(scenarios)
    )
)

# Compare the queue lengths for the different scenarios
compare_queue_lengths(scenarios)
