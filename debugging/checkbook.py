class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Ajoute le montant spécifié au solde."""
        self.balance += amount
        print("Montant déposé : ${:.2f}".format(amount))
        print("Solde actuel : ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Soustrait le montant spécifié du solde si les fonds sont suffisants."""
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Montant retiré : ${:.2f}".format(amount))
            print("Solde actuel : ${:.2f}".format(self.balance))

    def get_balance(self):
        """Affiche le solde actuel."""
        print("Solde actuel : ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("Que voulez-vous faire ? (deposit, withdraw, balance, exit) : ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Entrez le montant à déposer : $"))
                if amount < 0:
                    print("Veuillez entrer un montant positif.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer une valeur numérique.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Entrez le montant à retirer : $"))
                if amount < 0:
                    print("Veuillez entrer un montant positif.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer une valeur numérique.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
	