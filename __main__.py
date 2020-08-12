""" Save a draft as pdf in Download folder.
"""

import sys

from api import (
    Api,
    combine,
    is_exist,
    makedirs,
    raw_input,
    start,
    username,
    userprofile,
)


def save_pdf():
    try:
        session = Api()
        print("Author: recs")
        print("Maintainer: Rechdi Slimane ")
        print("Last update: 2020-05-06")
        session.check_valid_version("Solid Edge ST7", "Solid Edge 2019")
        user = username()
        print("\nUser: %s" % user)
        if user.lower() in [
            "alba",
            "bouc11",
            "lapc3",
            "peld6",
            "fouj3",
            "cotk2",
            "nunk",
            "beam",
            "boum3",
            "morm8",
            "benn2",
            "recs",
            "gils2",
            "albp",
            "tres2",
        ]:
            print("Autorized user ID")
        else:
            print("user with no valid permissions.")
            sys.exit()
        draft = session.active_document()
        print("part: %s" % draft.name)
        assert draft.name.lower().endswith(".dft"), (
            "This macro only works on .dft not %s" % draft.name[-4:]
        )

        pdf_file = draft.name[:-4] + ".pdf"
        print("PDF Name : %s" % pdf_file)
        print("%s" % userprofile())
        root_download = userprofile() + "\\Downloads" + "\\solidedgePDFs\\"
        if not is_exist(root_download):
            makedirs(root_download)
        new_name = combine(root_download, pdf_file)

    except AssertionError as err:
        print(err.args)

    except Exception as ex:
        print(ex.args)

    else:
        # Save the pdf in Downloads/solidedgePDFs.
        draft.SaveAs(NewName=new_name, FileFormat=False)
        print("%s saved in %s" % (pdf_file, root_download))
        start(new_name) # Open the pdf.


def prompt_exit():
    raw_input("\nPress any key to exit...")
    sys.exit()


def confirmation(func):
    response = raw_input(
        """Save PDF in your Downloads folder, (Press y/[Y] to proceed.):"""
    )
    if response.lower() in ["y"]:
        func()
        prompt_exit()
    elif response in ["*"]:
        func()
    else:
        sys.exit()


if __name__ == "__main__":
    confirmation(save_pdf)
