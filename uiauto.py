import uiautomator2 as u2
from ppadb.client import Client as AdbClient
import csv
import winsound
from time import sleep
# import more_itertools

client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("XMJ4C20526003060")
d = u2.connect('XMJ4C20526003060')  # get from "adb devices"


file = open("num.csv", "r")
csv_reader = csv.reader(file)
lists_from_csv = []
for row in csv_reader:
    lists_from_csv.append(row)
flat_list = []
for sublist in lists_from_csv:
    for item in sublist:
        flat_list.append(item)
print("*******************************************")
print(len(flat_list), " Items After Removing Duplicate Values")
print("*******************************************")

# d.app_start("com.nextiva.nextivaapp.android", use_monkey=True)
d(description="Chats List Tab").click()
d(text="SMS").click()
for num in flat_list:
    d(resourceId="com.nextiva.nextivaapp.android:id/fab_card").click()
    inx = flat_list.index(num)
    print(inx, " = ", num)
    d.send_keys(num)
    # d(text="Send to").click()
    # device.shell(f'input tap 400 500')
    d(resourceId="com.nextiva.nextivaapp.android:id/list_item_contact_layout").click()
    if d(text="Invalid SMS Number", resourceId="com.nextiva.nextivaapp.android:id/md_title").exists():  # Invalid Sms
        d(resourceId="com.nextiva.nextivaapp.android:id/md_buttonDefaultPositive").click()
        d.press("back")
        continue

#  if repeated msg exist
    # if d(resourceId="com.nextiva.nextivaapp.android:id/list_item_message_container").exists() and not d(resourceId="com.nextiva.nextivaapp.android:id/list_item_chat_message_failed_text_view").exists():
    #     d.press("back")
    #     sleep(1)
    #     d.press("back")
    #     continue

    d(description="Message Input",
      resourceId="com.nextiva.nextivaapp.android:id/chat_conversation_message_edit_text").click()

    d.send_keys("Hey!\nAre you interested in increasing your collection rate and getting Medicare, Medicaid,and all commercial payors enrollment? \nWe are offering guaranteed Credentialing and Contracting Services. \nWe can also help you to get the License from the State according to your degree/Specialty.\nWe also offer Medical Billing Services at 4.99% of the collected amount. Maximize revenues, increase collection, reduce expenses, and improve overall efficiency. There will be no upfront or hidden charges. \nRegards,\nBadar Noman\nE: badar@acemedassist.com\nw: www.acemedassist.com\n\n\nReply “Yes” if you’re interested")
    d(resourceId="com.nextiva.nextivaapp.android:id/chat_conversation_send_image_view").click()

    if d(resourceId="com.nextiva.nextivaapp.android:id/list_item_chat_message_failed_text_view").exists(timeout=4):

        d(resourceId="com.nextiva.nextivaapp.android:id/list_item_chat_message_sent_layout").click()

        if d(resourceId="com.nextiva.nextivaapp.android:id/md_title", text="No Internet Connection").exists():
            winsound.PlaySound("bell.wav", winsound.SND_FILENAME)
            break

        if d(resourceId="com.nextiva.nextivaapp.android:id/list_item_chat_message_failed_text_view").exists(timeout=3):
            winsound.PlaySound("bell.wav", winsound.SND_FILENAME)
            break

    d.press("back")
    d.press("back")
winsound.PlaySound("bell.wav", winsound.SND_FILENAME)


# d.dump_hierarchy("hierarchy.xml")
