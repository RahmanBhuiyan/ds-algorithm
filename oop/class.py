# class stack:
#     age=10
#     def __init__(self,age):
#         self.year=age
#     def chill(self,date):
#         self.__date=date
#         return self.__date
        
# db=stack(12)
# print(db.age)
# print(db.year) 
# print(db.chill("6pm")) 




# import time
# stack=[]
# def push(stack,user):
#     stack.append(user)
#     print("push your item",stack)
#     size=len(stack)
#     if size==10:
#         print("stack is full")
#     else:
#         print("stack is not full")
# push(stack,1)
# def pop(stack):
#     stack.pop(-1)
#     print("delate your item",stack)

# pop(stack)
     
struct node *head;
struct node *one = NULL;
struct node *two = NULL;
struct node *three = NULL;

/* Allocate memory */
one = malloc(sizeof(struct node));
two = malloc(sizeof(struct node));
three = malloc(sizeof(struct node));

/* Assign data values */
one->data = 1;
two->data = 2;
three->data=3;

/* Connect nodes */
one->next = two;
two->next = three;
three->next = NULL;

/* Save address of first node in head */
head = one;
