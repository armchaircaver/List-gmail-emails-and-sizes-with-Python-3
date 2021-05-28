# List-gmail-emails-and-sizes-with-Python-3
Efficiently read list of gmail emails and sizes with Python 3

Python script to list all emails in a gmail account, including the size of each email, 
in order to identify large emails and large numbers of  emails from a sender.

The script does not read the body of the email, just the sender, recipient, subject and size. 
It obtains all the emails in a single fetch, which is much more efficient than fetching data for each email individually.

On my laptop it can read and process approx 20,000 emails in a minute.
