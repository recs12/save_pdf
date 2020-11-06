"""
Api solidedge
=======================
"""

import clr
import sys

clr.AddReference("System")
clr.AddReference("System.IO")
clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import System.Runtime.InteropServices as SRI
import System
from System import Console
from System.Diagnostics.Process import Start
from System.IO.Path import Combine
from System.IO import Directory



def raw_input(message):
    Console.WriteLine(message)
    return Console.ReadLine()


def is_exist(path_to_check):
    return Directory.Exists(path_to_check)


def makedirs(path_to_make):
    Directory.CreateDirectory(path_to_make)


def userprofile():
    return System.Environment.GetEnvironmentVariable("USERPROFILE")


def username():
    return System.Environment.UserName


def combine(path1, path2):
    return Combine(path1, path2)


def prompt_exit():
    raw_input("\nPress any key to exit...")
    sys.exit()


def save_as_pdf(draft, open):
    """Print draft as pdf in a local folder in the Dowloads folder.
    """
    print("---")

    print("Drawing: %s" % draft.name)
    assert draft.name.lower().endswith(".dft"), (
        "This macro only works on Drawing document not %s" % draft.name[-4:]
    )
    pdf_file = draft.name[:-4] + ".pdf"

    print("PDF    : %s" % pdf_file)
    root_download = userprofile() + "\\Downloads" + "\\solidedgePDFs\\"
    if not is_exist(root_download):
        makedirs(root_download)

    # Save the pdf in Downloads/solidedgePDFs.
    new_name = combine(root_download, pdf_file)
    draft.SaveAs(NewName=new_name, FileFormat=False)
    if open:
        Start(new_name)  # Open the pdf.
    print("saved in %s" % root_download)
    print("...")
