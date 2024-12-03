import math
# M/M/1 Model
def mm1(lambd, mu):
    rho = lambd / mu
    if rho >= 1:
        return "Invalid! Utilization factor (ρ) should be less than 1 for M/M/1 model."
    
    lq = rho**2 / (1 - rho)
    wq = lq / lambd
    l = rho / (1 - rho)
    w = 1 / (mu - lambd)
    p0 = 1 - rho
    return lq, wq, l, w, p0

# M/M/c Model
def mmc(lambd, mu, c):
    rho = lambd / (c * mu)
    if rho >= 1:
        return "Invalid! Utilization factor (ρ) should be less than 1 for M/M/c model."
    
    r = lambd / mu
    summation = sum((r**i) / math.factorial(i) for i in range(c))
    p0 = 1 / (summation + (r**c / (math.factorial(c) * (1 - rho))))
    lq = (p0 * (r**c) * rho) / (math.factorial(c) * (1 - rho)**2)
    l = lq + r
    w = l / lambd
    wq = lq / lambd
    return lq, wq, l, w, p0

# M/M/1/K Model
def mm1k(lambd, mu, K):
    rho = lambd / mu

    if rho == 1:
        p0 = 1 / (1 + K)
        l = K / 2
        lq = (K * (K - 1)) / (2 * (K + 1))
    else:
        p0 = (1 - rho) / (1 - rho**(K + 1))
        l = rho * (1 - (K + 1) * rho**K + K * rho**(K + 1)) / ((1 - rho)**2 * (1 - rho**(K + 1)))
        lq = l - rho * (1 - (rho**K) * (K / (1 - rho**(K + 1))))
    
    pk = (rho**K) * p0
    lambd_eff = lambd * (1 - pk)
    w = l / lambd_eff
    wq = lq / lambd_eff
    return lq, wq, l, w, pk, p0

# Main Program
def queuing_models():
    print("Queuing Model Characteristics Calculator")
    print("1. M/M/1 Model")
    print("2. M/M/c Model")
    print("3. M/M/1/K Model")
    
    choice = int(input("Enter your choice (1-3): "))
    
    if choice == 1:
        lambd = float(input("Enter average arrival rate (λ): "))
        mu = float(input("Enter average service rate (μ): "))
        result = mm1(lambd, mu)
        if isinstance(result, str):
            print(result)
        else:
            lq, wq, l, w, p0 = result
            print(f"Lq (Average number in queue): {lq:.2f}")
            print(f"Wq (Average time in queue): {wq:.2f}")
            print(f"L (Average number in system): {l:.2f}")
            print(f"W (Average time in system): {w:.2f}")
            print(f"P0 (Probability of zero customers in system): {p0:.2f}")
    
    elif choice == 2:
        lambd = float(input("Enter average arrival rate (λ): "))
        mu = float(input("Enter average service rate (μ): "))
        c = int(input("Enter number of servers (c): "))
        result = mmc(lambd, mu, c)
        if isinstance(result, str):
            print(result)
        else:
            lq, wq, l, w, p0 = result
            print(f"Lq (Average number in queue): {lq:.2f}")
            print(f"Wq (Average time in queue): {wq:.2f}")
            print(f"L (Average number in system): {l:.2f}")
            print(f"W (Average time in system): {w:.2f}")
            print(f"P0 (Probability of zero customers in system): {p0:.2f}")
    
    elif choice == 3:
        lambd = float(input("Enter average arrival rate (λ): "))
        mu = float(input("Enter average service rate (μ): "))
        K = int(input("Enter system capacity (K): "))
        result = mm1k(lambd, mu, K)
        lq, wq, l, w, pk, p0 = result
        print(f"Lq (Average number in queue): {lq:.2f}")
        print(f"Wq (Average time in queue): {wq:.2f}")
        print(f"L (Average number in system): {l:.2f}")
        print(f"W (Average time in system): {w:.2f}")
        print(f"Pk (Probability of K customers in system): {pk:.2f}")
        print(f"P0 (Probability of zero customers in system): {p0:.2f}")
    
    else:
        print("Invalid choice! Please choose between 1-3.")
queuing_models()
