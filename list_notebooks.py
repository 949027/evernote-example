#!/usr/bin/env python
import os

from environs import Env
from evernote.api.client import EvernoteClient


if __name__ == '__main__':
    env = Env()
    env.read_env()
    client = EvernoteClient(
        token=env('EVERNOTE_PERSONAL_TOKEN'),
        sandbox=env.bool('SANDBOX'),
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print('%s - %s' % (notebook.guid, notebook.name))
