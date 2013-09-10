from datetime import datetime, date
import os
import sys


class NoteKeeper(object):
    
    def __init__(self):
        self.notes_dir = '/opt/notekeeper/'
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)
        self.filename = \
            "notes-{0}.txt".format(str(date.today()))
        self.full_path = self.notes_dir + self.filename

    def _save(self, note):
        with open(self.full_path, 'ab') as nf:
            timestamp = datetime.now().strftime("%H:%M:%S")
            nf.write("{0} => {1} \n".format(timestamp, note))
            nf.close()

    def _list_files(self, date=None):
        file_list = os.listdir(self.notes_dir)
        dates_to_notes = dict([(datetime.strptime(file_name[6:-4], '%Y-%m-%d'), file_name) \
                            for file_name in file_list])
        # for file_date in sorted(dates_to_notes.keys()):
        #     print "{0} => \n\t\t {1} \n ".format(file_date, dates_to_notes[file_date])
        # print "\n\n"
        self._list_detail(dates_to_notes)
    
    def _list_detail(self, _dict):
        choices = dict(zip(range(1,len(_dict)+1), _dict.keys()))
        while True:
            print "Choose note id to display:"
            for key, value in choices.iteritems():
                print "id {0} => {1}".format(key, str(value))
            choice = ''
            try:
                choice = raw_input("id to display: ")
            except KeyboardInterrupt:
                print "\nBye!"
                sys.exit(1)
            file_to_display = self.notes_dir + _dict[choices[int(choice)]]
            with open(file_to_display, 'rb') as f:
                for line in f.readlines():
                    print line
            print "\n\n"



    def run(self, note):
        self._save(note)
        self._list_files()

if __name__ == '__main__':
    nk = NoteKeeper()
    nk.run(sys.argv[1])
