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

    def run(self, note):
        self._save(note)

if __name__ == '__main__':
    nk = NoteKeeper()
    nk.run(sys.argv[1])
