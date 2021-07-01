from django.db import models

# Create your models here.
class Class(models.Model):
    Number = models.IntegerField()
    Section = models.CharField(max_length=2)

    Monday_0 = models.CharField(max_length=200, null=True, blank=True)
    Monday_1 = models.CharField(max_length=200, null=True, blank=True)
    Monday_2 = models.CharField(max_length=200, null=True, blank=True)
    Monday_3 = models.CharField(max_length=200, null=True, blank=True)
    Monday_4 = models.CharField(max_length=200, null=True, blank=True)
    Monday_5 = models.CharField(max_length=200, null=True, blank=True)
    Monday_6 = models.CharField(max_length=200, null=True, blank=True)
    Monday_7 = models.CharField(max_length=200, null=True, blank=True)
    Monday_8 = models.CharField(max_length=200, null=True, blank=True)
    
    Tuesday_0 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_1 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_2 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_3 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_4 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_5 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_6 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_7 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_8 = models.CharField(max_length=200, null=True, blank=True)

    Wednesday_0 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_1 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_2 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_3 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_4 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_5 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_6 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_7 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_8 = models.CharField(max_length=200, null=True, blank=True)

    Thursday_0 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_1 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_2 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_3 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_4 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_5 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_6 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_7 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_8 = models.CharField(max_length=200, null=True, blank=True)

    Friday_0 = models.CharField(max_length=200, null=True, blank=True)
    Friday_1 = models.CharField(max_length=200, null=True, blank=True)
    Friday_2 = models.CharField(max_length=200, null=True, blank=True)
    Friday_3 = models.CharField(max_length=200, null=True, blank=True)
    Friday_4 = models.CharField(max_length=200, null=True, blank=True)
    Friday_5 = models.CharField(max_length=200, null=True, blank=True)
    Friday_6 = models.CharField(max_length=200, null=True, blank=True)
    Friday_7 = models.CharField(max_length=200, null=True, blank=True)
    Friday_8 = models.CharField(max_length=200, null=True, blank=True)

    Saturday_0 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_1 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_2 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_3 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_4 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_5 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_6 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_7 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_8 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        Model_name = str(self.Number) + " " + str(self.Section)
        return Model_name


class Teacher(models.Model):
    classes = models.ManyToManyField(Class)

    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)

    Subject = models.CharField(max_length=100)

    Monday_0 = models.CharField(max_length=200, null=True, blank=True)
    Monday_1 = models.CharField(max_length=200, null=True, blank=True)
    Monday_2 = models.CharField(max_length=200, null=True, blank=True)
    Monday_3 = models.CharField(max_length=200, null=True, blank=True)
    Monday_4 = models.CharField(max_length=200, null=True, blank=True)
    Monday_5 = models.CharField(max_length=200, null=True, blank=True)
    Monday_6 = models.CharField(max_length=200, null=True, blank=True)
    Monday_7 = models.CharField(max_length=200, null=True, blank=True)
    Monday_8 = models.CharField(max_length=200, null=True, blank=True)
    
    Tuesday_0 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_1 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_2 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_3 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_4 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_5 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_6 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_7 = models.CharField(max_length=200, null=True, blank=True)
    Tuesday_8 = models.CharField(max_length=200, null=True, blank=True)

    Wednesday_0 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_1 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_2 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_3 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_4 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_5 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_6 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_7 = models.CharField(max_length=200, null=True, blank=True)
    Wednesday_8 = models.CharField(max_length=200, null=True, blank=True)

    Thursday_0 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_1 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_2 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_3 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_4 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_5 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_6 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_7 = models.CharField(max_length=200, null=True, blank=True)
    Thursday_8 = models.CharField(max_length=200, null=True, blank=True)

    Friday_0 = models.CharField(max_length=200, null=True, blank=True)
    Friday_1 = models.CharField(max_length=200, null=True, blank=True)
    Friday_2 = models.CharField(max_length=200, null=True, blank=True)
    Friday_3 = models.CharField(max_length=200, null=True, blank=True)
    Friday_4 = models.CharField(max_length=200, null=True, blank=True)
    Friday_5 = models.CharField(max_length=200, null=True, blank=True)
    Friday_6 = models.CharField(max_length=200, null=True, blank=True)
    Friday_7 = models.CharField(max_length=200, null=True, blank=True)
    Friday_8 = models.CharField(max_length=200, null=True, blank=True)

    Saturday_0 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_1 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_2 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_3 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_4 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_5 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_6 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_7 = models.CharField(max_length=200, null=True, blank=True)
    Saturday_8 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        Model_name = str(self.First_Name) + " " + str(self.Last_Name)
        return Model_name

    # @classmethod
    def create_timetable(self, classes):
        print ("skldjskjf called")
        print(self.id)
        sub = str(self.Subject)
        print (sub)
        for cla in classes:
            print ("in for loop")
            print (cla.id)
            cla_teacher = self.classes # self.objects.filter(classes__id = cla.id)
            print (cla_teacher)
            if cla_teacher is not None:
                mon_0 = str(cla.Monday_0)
                if sub in mon_0:
                    temp = ""
                    if mon_0 is not None:
                        temp = mon_0
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_0 = temp
                    self.save()
                    print(self.Monday_0)
                else:
                    temp = mon_0
                    try:
                        temp = mon_0.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Monday_0 = temp
                    self.save()
                    print(self.Monday_0)

                mon_1 = str(cla.Monday_1)
                if sub in mon_1:
                    temp = ""
                    if mon_1 is not None:
                        temp = mon_1
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_1 = temp
                    self.save()
                    print(self.Monday_1)
                else:
                    temp = mon_1
                    try:
                        temp = mon_1.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Monday_1 = temp
                    self.save()
                    print(self.Monday_1)

                mon_2 = str(cla.Monday_2)
                if sub in mon_2:
                    temp = ""
                    if mon_2 is not None:
                        temp = mon_2
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_2 = temp
                    self.save()
                    print(self.Monday_2)
                else:
                    temp = mon_2
                    try:
                        temp = mon_2.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Monday_2 = temp
                    self.save()
                    print(self.Monday_2)

                mon_3 = str(cla.Monday_3)
                if sub in mon_3:
                    temp = ""
                    if mon_3 is not None:
                        temp = mon_3
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_3 = temp
                    self.save()
                    print(self.Monday_3)

                mon_4 = str(cla.Monday_4)
                if sub in mon_4:
                    temp = ""
                    if mon_4 is not None:
                        temp = mon_4
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_4 = temp
                    self.save()
                    print(self.Monday_4)

                mon_5 = str(cla.Monday_5)
                if sub in mon_5:
                    temp = ""
                    if mon_5 is not None:
                        temp = mon_5
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_5 = temp
                    self.save()
                    print(self.Monday_5)

                mon_6 = str(cla.Monday_6)
                if sub in mon_6:
                    temp = ""
                    if mon_6 is not None:
                        temp = mon_6
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_6 = temp
                    self.save()
                    print(self.Monday_6)

                mon_7 = str(cla.Monday_7)
                if sub in mon_7:
                    temp = ""
                    if mon_7 is not None:
                        temp = mon_7
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_7 = temp
                    self.save()
                    print(self.Monday_7)

                mon_8 = str(cla.Monday_8)
                if sub in mon_8:
                    temp = ""
                    if mon_8 is not None:
                        temp = mon_8
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Monday_8 = temp
                    self.save()
                    print(self.Monday_8)

                Tues_0 = str(cla.Tuesday_0)
                if sub in Tues_0:
                    temp = ""
                    if Tues_0 is not None:
                        temp = Tues_0
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_0 = temp
                    self.save()
                    print(self.Tuesday_0)
                else:
                    temp = Tues_0
                    try:
                        temp = Tues_0.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Tuesday_0 = temp
                    self.save()
                    print(self.Tuesday_0)

                Tues_1 = str(cla.Tuesday_1)
                if sub in Tues_1:
                    temp = ""
                    if Tues_1 is not None:
                        temp = Tues_1
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_1 = temp
                    self.save()
                    print(self.Tuesday_1)
                else:
                    temp = Tues_1
                    try:
                        temp = Tues_1.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Tuesday_1 = temp
                    self.save()
                    print(self.Tuesday_1)

                Tues_2 = str(cla.Tuesday_2)
                if sub in Tues_2:
                    temp = ""
                    if Tues_2 is not None:
                        temp = Tues_2
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_2 = temp
                    self.save()
                    print(self.Tuesday_2)
                else:
                    temp = Tues_2
                    try:
                        temp = Tues_2.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Tuesday_2 = temp
                    self.save()
                    print(self.Tuesday_2)

                Tues_3 = str(cla.Tuesday_3)
                if sub in Tues_3:
                    temp = ""
                    if Tues_3 is not None:
                        temp = Tues_3
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_3 = temp
                    self.save()
                    print(self.Tuesday_3)
                else:
                    temp = Tues_3
                    try:
                        temp = Tues_3.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Tuesday_3 = temp
                    self.save()
                    print(self.Tuesday_3)

                Tues_4 = str(cla.Tuesday_4)
                if sub in Tues_4:
                    temp = ""
                    if Tues_4 is not None:
                        temp = Tues_4
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_4 = temp
                    self.save()
                    print(self.Tuesday_4)
                else:
                    temp = Tues_4
                    try:
                        temp = Tues_4.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Tuesday_4 = temp
                    self.save()
                    print(self.Tuesday_4)

                Tues_5 = str(cla.Tuesday_5)
                if sub in Tues_5:
                    temp = ""
                    if Tues_5 is not None:
                        temp = Tues_5
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_5 = temp
                    self.save()
                    print(self.Tuesday_5)

                Tues_6 = str(cla.Tuesday_6)
                if sub in Tues_6:
                    temp = ""
                    if Tues_6 is not None:
                        temp = Tues_6
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_6 = temp
                    self.save()
                    print(self.Tuesday_6)

                Tues_7 = str(cla.Tuesday_7)
                if sub in Tues_7:
                    temp = ""
                    if Tues_7 is not None:
                        temp = Tues_7
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_7 = temp
                    self.save()
                    print(self.Tuesday_7)

                Tues_8 = str(cla.Tuesday_8)
                if sub in Tues_8:
                    temp = ""
                    if Tues_8 is not None:
                        temp = Tues_8
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Tuesday_8 = temp
                    self.save()
                    print(self.Tuesday_8)

                Wednes_0 = str(cla.Wednesday_0)
                if sub in Wednes_0:
                    temp = ""
                    if Wednes_0 is not None:
                        temp = Wednes_0
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_0 = temp
                    self.save()
                    print(self.Wednesday_0)
                else:
                    temp = Wednes_0
                    try:
                        temp = Wednes_0.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Wednesday_0 = temp
                    self.save()
                    print(self.Wednesday_0)

                Wednes_1 = str(cla.Wednesday_1)
                if sub in Wednes_1:
                    temp = ""
                    if Wednes_1 is not None:
                        temp = Wednes_1
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_1 = temp
                    self.save()
                    print(self.Wednesday_1)
                else:
                    temp = Wednes_1
                    try:
                        temp = Wednes_1.replace(str(cla.Number + ' ' + cla.Section), '')
                    except:
                        pass
                    print(temp)
                    self.Wednesday_1 = temp
                    self.save()
                    print(self.Wednesday_1)

                Wednes_2 = str(cla.Wednesday_2)
                if sub in Wednes_2:
                    temp = ""
                    if Wednes_2 is not None:
                        temp = Wednes_2
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_2 = temp
                    self.save()
                    print(self.Wednesday_2)

                Wednes_3 = str(cla.Wednesday_3)
                if sub in Wednes_3:
                    temp = ""
                    if Wednes_3 is not None:
                        temp = Wednes_3
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_3 = temp
                    self.save()
                    print(self.Wednesday_3)

                Wednes_4 = str(cla.Wednesday_4)
                if sub in Wednes_4:
                    temp = ""
                    if Wednes_4 is not None:
                        temp = Wednes_4
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_4 = temp
                    self.save()
                    print(self.Wednesday_4)

                Wednes_5 = str(cla.Wednesday_5)
                if sub in Wednes_5:
                    temp = ""
                    if Wednes_5 is not None:
                        temp = Wednes_5
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_5 = temp
                    self.save()
                    print(self.Wednesday_5)

                Wednes_6 = str(cla.Wednesday_6)
                if sub in Wednes_6:
                    temp = ""
                    if Wednes_6 is not None:
                        temp = Wednes_6
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_6 = temp
                    self.save()
                    print(self.Wednesday_6)

                Wednes_7 = str(cla.Wednesday_7)
                if sub in Wednes_7:
                    temp = ""
                    if Wednes_7 is not None:
                        temp = Wednes_7
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_7 = temp
                    self.save()
                    print(self.Wednesday_7)

                Wednes_8 = str(cla.Wednesday_8)
                if sub in Wednes_8:
                    temp = ""
                    if Wednes_8 is not None:
                        temp = Wednes_8
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Wednesday_8 = temp
                    self.save()
                    print(self.Wednesday_8)

                Thurs_0 = str(cla.Thursday_0)
                if sub in Thurs_0:
                    temp = ""
                    if Thurs_0 is not None:
                        temp = Thurs_0
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_0 = temp
                    self.save()
                    print(self.Thursday_0)

                Thurs_1 = str(cla.Thursday_1)
                if sub in Thurs_1:
                    temp = ""
                    if Thurs_1 is not None:
                        temp = Thurs_1
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_1 = temp
                    self.save()
                    print(self.Thursday_1)

                Thurs_2 = str(cla.Thursday_2)
                if sub in Thurs_2:
                    temp = ""
                    if Thurs_2 is not None:
                        temp = Thurs_2
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_2 = temp
                    self.save()
                    print(self.Thursday_2)

                Thurs_3 = str(cla.Thursday_3)
                if sub in Thurs_3:
                    temp = ""
                    if Thurs_3 is not None:
                        temp = Thurs_3
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_3 = temp
                    self.save()
                    print(self.Thursday_3)

                Thurs_4 = str(cla.Thursday_4)
                if sub in Thurs_4:
                    temp = ""
                    if Thurs_4 is not None:
                        temp = Thurs_4
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_4 = temp
                    self.save()
                    print(self.Thursday_4)

                Thurs_5 = str(cla.Thursday_5)
                if sub in Thurs_5:
                    temp = ""
                    if Thurs_5 is not None:
                        temp = Thurs_5
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_5 = temp
                    self.save()
                    print(self.Thursday_5)

                Thurs_6 = str(cla.Thursday_6)
                if sub in Thurs_6:
                    temp = ""
                    if Thurs_6 is not None:
                        temp = Thurs_6
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_6 = temp
                    self.save()
                    print(self.Thursday_6)

                Thurs_7 = str(cla.Thursday_7)
                if sub in Thurs_7:
                    temp = ""
                    if Thurs_7 is not None:
                        temp = Thurs_7
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_7 = temp
                    self.save()
                    print(self.Thursday_7)

                Thurs_8 = str(cla.Thursday_8)
                if sub in Thurs_8:
                    temp = ""
                    if Thurs_8 is not None:
                        temp = Thurs_8
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Thursday_8 = temp
                    self.save()
                    print(self.Thursday_8)

                Fri_0 = str(cla.Friday_0)
                if sub in Fri_0:
                    temp = ""
                    if Fri_0 is not None:
                        temp = Fri_0
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_0 = temp
                    self.save()
                    print(self.Friday_0)

                Fri_1 = str(cla.Friday_1)
                if sub in Fri_1:
                    temp = ""
                    if Fri_1 is not None:
                        temp = Fri_1
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_1 = temp
                    self.save()
                    print(self.Friday_1)

                Fri_2 = str(cla.Friday_2)
                if sub in Fri_2:
                    temp = ""
                    if Fri_2 is not None:
                        temp = Fri_2
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_2 = temp
                    self.save()
                    print(self.Friday_2)

                Fri_3 = str(cla.Friday_3)
                if sub in Fri_3:
                    temp = ""
                    if Fri_3 is not None:
                        temp = Fri_3
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_3 = temp
                    self.save()
                    print(self.Friday_3)

                Fri_4 = str(cla.Friday_4)
                if sub in Fri_4:
                    temp = ""
                    if Fri_4 is not None:
                        temp = Fri_4
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_4 = temp
                    self.save()
                    print(self.Friday_4)

                Fri_5 = str(cla.Friday_5)
                if sub in Fri_5:
                    temp = ""
                    if Fri_5 is not None:
                        temp = Fri_5
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_5 = temp
                    self.save()
                    print(self.Friday_5)

                Fri_6 = str(cla.Friday_6)
                if sub in Fri_6:
                    temp = ""
                    if Fri_6 is not None:
                        temp = Fri_6
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_6 = temp
                    self.save()
                    print(self.Friday_6)

                Fri_7 = str(cla.Friday_7)
                if sub in Fri_7:
                    temp = ""
                    if Fri_7 is not None:
                        temp = Fri_7
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_7 = temp
                    self.save()
                    print(self.Friday_7)

                Fri_8 = str(cla.Friday_8)
                if sub in Fri_8:
                    temp = ""
                    if Fri_8 is not None:
                        temp = Fri_8
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Friday_8 = temp
                    self.save()
                    print(self.Friday_8)

                Satur_0 = str(cla.Saturday_0)
                if sub in Satur_0:
                    temp = ""
                    if Satur_0 is not None:
                        temp = Satur_0
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_0 = temp
                    self.save()
                    print(self.Saturday_0)

                Satur_1 = str(cla.Saturday_1)
                if sub in Satur_1:
                    temp = ""
                    if Satur_1 is not None:
                        temp = Satur_1
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_1 = temp
                    self.save()
                    print(self.Saturday_1)

                Satur_2 = str(cla.Saturday_2)
                if sub in Satur_2:
                    temp = ""
                    if Satur_2 is not None:
                        temp = Satur_2
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_2 = temp
                    self.save()
                    print(self.Saturday_2)

                Satur_3 = str(cla.Saturday_3)
                if sub in Satur_3:
                    temp = ""
                    if Satur_3 is not None:
                        temp = Satur_3
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_3 = temp
                    self.save()
                    print(self.Saturday_3)

                Satur_4 = str(cla.Saturday_4)
                if sub in Satur_4:
                    temp = ""
                    if Satur_4 is not None:
                        temp = Satur_4
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_4 = temp
                    self.save()
                    print(self.Saturday_4)

                Satur_5 = str(cla.Saturday_5)
                if sub in Satur_5:
                    temp = ""
                    if Satur_5 is not None:
                        temp = Satur_5
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_5 = temp
                    self.save()
                    print(self.Saturday_5)

                Satur_6 = str(cla.Saturday_6)
                if sub in Satur_6:
                    temp = ""
                    if Satur_6 is not None:
                        temp = Satur_6
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_6 = temp
                    self.save()
                    print(self.Saturday_6)

                Satur_7 = str(cla.Saturday_7)
                if sub in Satur_7:
                    temp = ""
                    if Satur_7 is not None:
                        temp = Satur_7
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_7 = temp
                    self.save()
                    print(self.Saturday_7)

                Satur_8 = str(cla.Saturday_8)
                if sub in Satur_8:
                    temp = ""
                    if Satur_8 is not None:
                        temp = Satur_8
                    temp = " " + str(cla.Number) + " " + str(cla.Section)
                    print(temp)
                    self.Saturday_8 = temp
                    self.save()
                    print(self.Saturday_8)