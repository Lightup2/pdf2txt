import os
import PyPDF2
from multiprocessing import Pool
from tqdm import tqdm
path = "G:/年报/"
path_result = "G:/年报txt/"
os.chdir(path)#os.chdir() 方法用于改变当前工作目录到指定的路径
dirlist = os.listdir(path)

for p in dirlist:
    path2 = path+p
    dirlist2 = os.listdir(path2)
    for j in dirlist2:
        k = j.split('.')[0]
        # print(k)

def dir_pdf2txt(dir_name):
    path_new = path+dir_name
    dirlist = os.listdir(path_new)
    file_path = path_result + dir_name
    if os.path.isdir(file_path):
        pass
    else:
        os.mkdir(file_path)  
    for j in dirlist:
        namelist=j.split('.')
        namelist[-1]="txt"
        txt_name='.'.join(namelist)
        # k = j.split('.')[0]
        pdf_filename = path+dir_name+"/"+j
        txt_filename = path_result+dir_name+"/"+txt_name
        if os.path.isfile(txt_filename):
            continue
        else:
            with open(pdf_filename, 'rb') as pdfFileObj:
                pdfReader = PyPDF2.PdfReader(pdfFileObj)
                x=pdfReader.numPages
                try:
                    with open(txt_filename,"a",encoding='utf-8') as file1:
                        for i in range(x):
                            pageobj=pdfReader.pages[i]
                            text=pageobj.extract_text()
                            file1.writelines(text)
                except:
                    with open(path_result+"异常文件.csv","a",encoding='utf-8') as file2:
                        file2.write('%s\n' % (pdf_filename))


if __name__=="__main__":
    with Pool(6) as par:
        for _ in tqdm(par.imap_unordered(dir_pdf2txt,dirlist) , total=len(dirlist),bar_format='{l_bar}{bar:50}{r_bar}{bar:-10b}'):
            pass