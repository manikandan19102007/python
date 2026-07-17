class song:
    def __init__(self,song):
        self.song=song
        self.next=None
def display(head):
    temp=head
    while temp is not None:
        print(temp.song,end="\n")
        temp=temp.next
    print("None")
s1=song("Poongatrile")
s2=song("Rasathi")
s3=song("konja naal")
s4=song("siragugal")
s5=song("saratu vandi")
s1.next=s2
s2.next=s3
s3.next=s4
s4.next=s5
head=s1
#insert beginning
s0=song("uyire uyire")
s0.next=head
head=s0
print("\nInsert at beginning:")
display(head)
#insert end
s6=song("roja")
temp=head
while temp.next is not None:
    temp=temp.next
temp.next=s6
print("\nInsert at end:")
display(head)
#insert middle
temp=head
s7=song("Narumugaye")
while temp is not None and temp.song!="konja naal":
    temp=temp.next
s7.next=temp.next
temp.next=s7
print("\nInsert at middle:")
display(head)
#delete at beginning
head=head.next
print("\nDeletion at beginning:")
display(head)
#delete at end
temp=head
while temp.next.next is not None:
    temp=temp.next
temp.next=None
print("\nDeletion at end:")
display(head)
#delete at middle
temp=head
while temp.next is not None and temp.next.song!="konja naal":
    temp=temp.next
if temp.next is not None:
    temp.next=temp.next.next
print("\nDeletion of middle element:")
display(head)
