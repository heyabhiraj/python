import math
class QueueingModel:
    def __init__(self, arrival_rate, service_rate, num_servers=1):
        self.lmbda = arrival_rate  #Arrival rate of customers per unit time
        self.mu = service_rate      #Service rate of customers per unit time
        self.c = num_servers        #Number of servers

    def mm1(self):
        # M/M/1 Queue
        rho = self.lmbda / self.mu  #Traffic Intensity
        if rho >= 1:
            return "System is unstable since arrival rate is greater than service rate)."
        
        # Average number of customers in the system
        L = rho / (1 - rho)
        # Average time a customer spends in the system
        W = 1 / (self.mu - self.lmbda)
        return L, W

    def mmc(self):
        # M/M/c Queue
        rho = self.lmbda / (self.c * self.mu)  # Utilization
        if rho >= 1:
            return "System is unstable since arrival rate is greater than service rate)."
        
        # Calculate the probability that no customers are in the system (P0)
        P0 = self._calculate_p0(rho)

        # Average number of customers in the queue
        Lq = (P0 * (self.lmbda**self.c) * rho) / (math.factorial(self.c) * (1 - rho)**2)
        # Average number of customers in the system
        L = Lq + self.lmbda / self.mu
        # Average time a customer spends in the system
        W = L / self.lmbda
        return L, W

    def _calculate_p0(self, rho):
        # Calculate P0 for the M/M/c queue
        sum_terms = sum((self.lmbda / self.mu)**n / math.factorial(n) for n in range(self.c))
        last_term = ((self.lmbda / self.mu)**self.c) / (math.factorial(self.c) * (1 - rho))
        return 1 / (sum_terms + last_term)


# Main Program
arrival_rate = float(input("Enter the arrival rate (lambda): "))
service_rate = float(input("Enter the service rate (mu): "))
num_servers = int(input("Enter the number of servers (for M/M/c, enter c): "))

model = QueueingModel(arrival_rate, service_rate, num_servers)

# Calculate and display results for M/M/1 Model
print("\n--- M/M/1 Queue Characteristics ---")
result_mm1 = model.mm1()
if isinstance(result_mm1, str):
    print(result_mm1)
else:
    L1, W1 = result_mm1
    print(f"Average number of customers in the system (L): {L1:.2f}")
    print(f"Average time spent in the system (W): {W1:.2f}")

# Calculate and display results for M/M/c Model
print("\n--- M/M/c Queue Characteristics ---")
result_mmc = model.mmc()
if isinstance(result_mmc,str):
    print(result_mmc)
else:
    L2, W2 = result_mmc
    print(f"Average number of customers in the system (L): {L2:.2f}")
    print(f"Average time spent in the system (W): {W2:.2f}")