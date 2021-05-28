import imaplib
import email
import time

def read_email_from_gmail(email_address, password, output_file):
  start = time.perf_counter()
  
  mail = imaplib.IMAP4_SSL("imap.gmail.com") # defaults to port 993
  try:
    mail.login(email_address,password)
  except:
    print("To use this script, the google account has to have",
          "less secure app access enabled :\n\n",
          "manage your google account > security > Less secure app access\n\n",
          "(or maybe the email_address / password is incorrect)")
    raise
  
  mail.select( '"[Gmail]/All Mail"' ) # note the quotation marks around the string, needed as it contains spaces

  # fetch results for all emails in a single fetch, much more efficient than a fetch for each email 
  _,results = mail.fetch('1:*', '(rfc822.size body[header.fields (from to subject date)])' )

  print("fetched ",len(results)//2,"messages, now processing and writing to output file...")

  # open the output file utf-8 encoding to cater for utf-8 characters in the email fields
  file = open(output_file,"w",encoding='utf-8')
  
  for msg in results:

    # we appear to get an additional message just containing ")" for each real message. Ignore these.
    if (len(msg)==1):
      continue

    # get the message size from the first part
    msg_size = msg[0].decode("utf-8").split()[2]
    
    # Parse the raw email message , and extract fields, removing any characters that might leg up an import into excel
    message = email.message_from_bytes(msg[1])

    date = message["date"]
    sender = str(message["from"]).replace("\n"," ").replace("\t"," ").replace("\r"," ")
    to = str(message["to"]).replace("\n"," ").replace("\t"," ").replace("\n"," ").replace("\t"," ").replace("\r"," ")
    subject = str(message["subject"]).replace("\n"," ").replace("\t"," ").replace("\n"," ").replace("\t"," ").replace("\r"," ")

    # print the fields tab separated, so that they can be copied and pasted into excel
    file.write (msg_size+ "\t"+ date+"\t"+ sender+"\t"+ to+"\t"+ subject +"\n")

  file.close()

  end = time.perf_counter()
  print( output_file, " created, ", end-start, "sec")

if __name__ == "__main__":

  # this isn't a real email address / password. Replace it with your own email address and password (and output file)
  read_email_from_gmail("donaldtrump@gmail.com","covfefe" , "donaldsemails.txt")
