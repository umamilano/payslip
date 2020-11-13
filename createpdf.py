import datetime
import os
from fpdf import FPDF

pdf_w = 210
pdf_h = 297
tanggal = datetime.datetime.now()
dn = os.path.dirname(os.path.realpath(__file__))

def resouce_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

class PDF(FPDF):

    def __init__(self):
        super().__init__()
        self.add_font("Arial Unicode", style="", fname=resouce_path("Arial Unicode MS.ttf"), uni=True)
        self.add_font("Arial Unicode Bold",style="B",fname=resouce_path("Arial Unicode Bold.ttf"), uni=True)

    def logopda(self):
        self.set_xy(155.0,6.0)
        self.image(name = 'logo.jpg',  link='', type='',w=3586/80)
        self.set_xy(51.0,17.0)
        self.set_font('Arial','',12)
        self.set_text_color(0,0,0)
        self.cell(w = 210.0 , h = 40.0, align = 'C', txt = "Maisonette Mega Kebon Jeruk Unit 12 & 15", border=0)
        self.text(x = 131.0 , y = 42.9, txt = "Jl. Raya Joglo Jakarta Barat 11640")
        self.text(x = 137.5 , y = 47.8, txt = "Phone: 021-5858 276 (Hunting)")
        self.text(x = 158.9 , y = 52.8, txt = "Fax: 021-5890 8225")

    def logoayn(self):
        self.set_xy(10.0,6.0)
        self.image(name =resouce_path("logo2.jpg"),  link='', type='',w=3586/80)
        self.set_font('Arial','B',12.1)
        self.set_text_color(132,61,148)
        self.text(x = 131.0 , y = 12.9, txt = "PT ALIHDAYA SARANA SUKSES")
        self.set_font('Arial','',8)
        self.set_text_color(0,0,0)
        alamat = ["FINANCE & ACCOUNTING","Maisonette Mega Kebon Jeruk Unit 12 & 15","Jl. Raya Joglo Jakarta Barat 11640","TEL: 021-5858 276 (Hunting) FAX: 021-5890 8525"]
        x_alamat , y_alamat = 131.0 , 17.9
        for address in alamat:
            self.text(x = x_alamat, y = y_alamat, txt = address.upper())
            y_alamat += 4

    def titles(self,periode):
        self.set_xy(0.0,40.0)
        self.set_font('Arial','B',16)
        self.set_text_color(0,0,0)
        self.cell(w = 210.0 , h = 15.0, align = 'C', txt = "SALARY SLIP", border=0)
        self.set_xy(0.0,47.9)
        self.set_font('Arial Unicode','',10)
        self.cell(w = 210.0, h = 10.0, align= 'C',txt= periode+tanggal.strftime(" %Y"),border=0)
        self.set_line_width(0.0)
        self.line(86.5,50,123,50)

    def detail_owner(self,nama):
        self.set_font('Arial Unicode','',12)
        self.text(x = 10., y = 65. , txt = "NAME              :  " + nama.upper())
        self.text(x = 10., y = 70., txt = "POSITION       :  STAFF")

    def income(self,b_salary,transport,comm,overtime,allowance):
        x_materi, y_materi = 25. , 89.
        x_cell, y_cell = 105. , 84.
        self.set_font('Arial Unicode','',12)
        materi = ['Basic Salary','Transport',"Phone's Credit","Overtime","Allowance etc"]
        materi_value = [b_salary,transport,comm,overtime,allowance]
        materi_rp = [format(i,",.2f")for i in materi_value]
        global total_income
        total_income = sum(materi_value)

        for x in materi:
            self.text(x = x_materi,y = y_materi, txt = x )
            self.text(x = x_materi+90 ,y= y_materi, txt ='Rp.')
            y_materi += 8
        for nilai in materi_rp:
            self.set_xy(x_cell,y_cell)
            self.cell(w = 50., h= 8., align ='R',txt=nilai,border=0)
            y_cell += 8
        self.set_line_width(0.0)
        self.line(115.,125,196,125)
        self.set_font('Arial Unicode Bold','B',12)
        self.text(x = x_materi+30, y =130., txt='Total Income')
        self.text(x = x_materi+130 ,y= 130., txt ='Rp.')
        self.text(x = 22.6, y = 82., txt = u'\u2022'+" INCOME")
        self.set_xy(146.,125.)
        self.cell(w = 50., h = 8., align='R',txt=format(total_income,",.2f"),border=0)

    def deduction(self,tk,ks,dp,admin,other):
        x_materi, y_materi = 25. , 149.
        x_cell, y_cell = 105. , 144.
        self.set_font('Arial Unicode','',12)
        materi = ['BPJS TK 2%','BPJS KS 1%',"BPJS DP 1%","Admin Bank","Other"]
        materi_value = [tk,ks,dp,admin,other]
        materi_rp = [format(i,",.2f")for i in materi_value]
        global total_deduction
        total_deduction = sum(materi_value)

        for x in materi:
            self.text(x = x_materi,y = y_materi, txt = x )
            self.text(x = x_materi+90 ,y= y_materi, txt ='Rp.')
            y_materi += 8
        for nilai in materi_rp:
            self.set_xy(x_cell,y_cell)
            self.cell(w = 50., h= 8., align ='R',txt=nilai,border=0)
            y_cell += 8
        self.set_line_width(0.0)
        self.line(115.,185,196,185)
        self.set_font('Arial Unicode Bold','B',12)
        self.text(x = x_materi+30, y =190., txt='Total Deduction')
        self.text(x = x_materi+130 ,y= 190., txt ='Rp.')
        self.text(x = 22.6, y = 142., txt = u'\u2022'+" DEDUCTION")
        self.set_xy(146.,185.)
        self.cell(w = 50., h = 8., align='R',txt=format(total_deduction,",.2f"),border=0)


    def thp(self):
        self.dashed_line(115, 210, 196, 210, 3, 3)
        self.set_font('Arial Unicode Bold','B',12)
        self.text(x = 22.6, y = 215., txt = u'\u2022'+" THP ( Income - Deduction )")
        self.text(x = 155. ,y= 215., txt ='Rp.')
        self.set_xy(146.,210.)
        self.cell(w = 50., h = 8., align='R',txt=format(total_income-total_deduction,",.2f"),border=0)

    def signature(self):
        self.set_font('Arial','',11)
        self.text(x = 10., y = 250 , txt ='Prepared by : Irfan Maulana Ishak')
        self.set_font('Arial','I',11)
        self.text(x = 10., y = 275 , txt ='This is a computer generated payslip and no signature is required')
        self.text(x = 10., y = 280 , txt ='Contact us for any details')


    def lines(self):
        self.set_line_width(0.0)
        self.line(0,pdf_h/2,210,pdf_h/2)
