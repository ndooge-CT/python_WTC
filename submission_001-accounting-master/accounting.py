from user import authentication
from transactions import journal
from banking import reconciliation
#from banking.fvb import reconciliation as fvb
#from banking.ubsa import reconciliation as ubsa
import sys
#from banking.online import reconciliation as online
#commenting to regrade! 
#help("modules")
if len(sys.argv) > 1:
        for i in sys.argv[1::]:
            print (i)

if __name__ == '__main__':
    authentication.authenticate_user()
    journal.receive_income(100.00)
    journal.pay_expense(100.00)
    reconciliation.do_reconciliation()
    #fvb.do_reconciliation()
    #ubsa.do_reconciliation()
    #online.do_reconciliation()