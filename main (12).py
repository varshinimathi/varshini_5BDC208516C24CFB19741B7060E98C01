class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
   self.__account_number=account_number
   self.__account_holder_name=account_holder_name
   self.__account_holder_name=account_holder_name
   self.__account_balance=initial_balance
  def deposite(self,amount):
    if amount>0:
      self.__account_balance+=amount
      print("Deposited ${}.New balance:$ {}".format(amount,self.__account_balance))
    else:
      print("Invalid deposite amount.")
      def withdraw(self,amount):
        if amount>0 and amount<=self.__account_balance:
          self.__account_balance-=amountprint("Withdraw$ {}.Newbalance:${}".format(amount,self.__account_balance))
        else:
          print("Invalid withdraw amount or insufficient balance.")
          def display_balance(self):
            print("Account balance for {}(account #{}):${}".format(self._account_holder_name,self._account_number,self.__account_balance))
            account=BankAccount(account_number="123456789",account_holder_name="maha",initial_balance=5000.0)
            account.display_balance()
            account.deposite(5000.0)
            account.withdraw(200.)
            account.display_balance()