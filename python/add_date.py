""" Command (with key-binding ctrl + s) that automatically updates
the date-last-modified section in a file with each save

Only thing the user has to change (if they so wish) is the variables
Header_Format and/or Date_Format """


import sublime, sublime_plugin
import time

class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, args):
        content = self.view.substr(sublime.Region(0, self.view.size()))

        """Can change Header_Format if you so wish.
        Don't worry about whether you have to add an extra space 
        at the end of 'Header_Format'; the rest of the code already
        takes care of that. """
        Header_Format = 'Last Modified:'

        begin = content.find(Header_Format)
        if begin == -1:
            return

        """ If you want your date printed out in a different format
            (e.g. YYYY/mm/dd instead of dd mm YYYY), feel free to 
            play around with the parameters in strftime() """
        Date_Format = time.strftime("%B %d, %Y")

        # To update time/date last modified, command looks for the beginning
        # of the date-string (e.g. "D" if it's "Date Last Edited: 26 Jun 2017 05:38PM") and 
        # the end of the date-string (e.g. "M" if it's "Date Last Edited: 26 Jun 2017 05:38PM")
        # and replaces the whole string with an identical string (only change being the time/date)

        # "+ 1" is to take into account the space between Header_Format and Date_Format
        length_of_line = len(Header_Format) + 1 + len(Date_Format)
        end = begin + length_of_line

        target_region = sublime.Region(begin, end)
        self.view.sel().clear()
        self.view.sel().add(target_region)

        # The " " adds a space between Header_Format and Date_Format
        self.view.run_command("insert_snippet", { "contents": Header_Format + " " + Date_Format } )
    

# Command does 2 things; update the date, and save the file
class DateAndSaveCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("add_date")
        self.window.run_command("save")