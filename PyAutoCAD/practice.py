from pyautocad import Autocad, APoint
import win32com.client
acad = win32com.client.Dispatch("AutoCAD.Application")

# acad = Autocad(create_if_not_exists=True)
# acad.prompt("Hello, Autocad from Python\n")
# print (acad.doc.Name)

# p1 = APoint(0, 0)
# p2 = APoint(50, 25)
# for i in range(5):
#     text = acad.model.AddText('Hi %s!' % i, p1, 2.5)
#     acad.model.AddLine(p1, p2)
#     acad.model.AddCircle(p1, 10)
#     p1.y += 10

# dp = APoint(10, 0)
# for text in acad.iter_objects('Text'):
#     print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
#     text.InsertionPoint = APoint(text.InsertionPoint) + dp

# for obj in acad.iter_objects(['Circle', 'Line','bCircle']):
#     print(obj.ObjectName)

for entity in acad.ActiveDocument.ModelSpace:
    name = entity.EntityName
    if name == 'AcDbBlockReference':
        HasAttributes = entity.HasAttributes
        if HasAttributes:
            for attrib in entity.GetAttributes():
                print("  {}: {}".format(attrib.TagString, attrib.TextString))
        else:
            print ('no atrribs')
