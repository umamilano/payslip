from createpdf import PDF
import pandas as pd
import datetime
import time
import os

lokasi = input("Enter database.xlsx location = ") + "\\"

tanggal = datetime.datetime.today()
save_folder = tanggal.strftime('%Y%m%d')
print('\nCreating folder',save_folder,'to save payslip PDF....')
time.sleep(2)
output = lokasi+save_folder
try:
    os.mkdir(output)
except:
    print('Folder',save_folder,'already exist')
else:
    print('Success create',save_folder,'folder')

data = pd.read_excel(lokasi+'database.xlsx')
karyawan = data['NAMA'].tolist()
b_salary = data['BASIC SALARY'].tolist()
transport = data['TRANSPORT'].tolist()
credit = data['COMM'].tolist()
lembur = data['OVERTIME'].tolist()
tunjangan = data['ALLOWANCE'].tolist()
bpjs_tk = data['TK'].tolist()
bpjs_ks = data['KS'].tolist()
bpjs_dp = data['DP'].tolist()
admin = data['ADMIN'].tolist()
lain = data['OTHER'].tolist()
periode = data['PERIODE'].tolist()

print('\nCreating Payslip from database...')
time.sleep(1)
for n in range(len(karyawan)):
    slip = PDF()
    slip.add_page()
    slip.logoayn()
    slip.titles(periode[n])
    slip.detail_owner(karyawan[n].upper())
    slip.income(b_salary[n],transport[n],credit[n],lembur[n],tunjangan[n])
    slip.deduction(bpjs_tk[n],bpjs_ks[n],bpjs_dp[n],admin[n],lain[n])
    slip.thp()
    slip.signature()
    slip.output(output+'\\PAYSLIP_'+karyawan[n].upper()+'.pdf','F')
    print("\n\tSuccess create payslip",karyawan[n].upper())
    time.sleep(1)
