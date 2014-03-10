from vclouddirector.action.client import ActionClient
from vclouddirector.session.behaviors import SessionBehaviors
from vclouddirector.model.org import Org


sb = SessionBehaviors(url="https://vcd.lab.ord1.pc.rackspace.com/api")
auth_token = sb.authenticate(user="qe_user", org="system", password="aUgHye1nP")

default_headers = {'accept': 'application/*+xml;version=1.5', 'x-vcloud-authorization': auth_token}

org = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/org")

response = org.execute_get(headers=default_headers)

print response.content

org1 = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/org/51a0dd22-bc5c-403f-971f-fd6270a9972b")

response = org1.execute_get(headers=default_headers)

print "****1"
print response.content

#roleRetrieve = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin")
#print roleRetrieve.execute_get(headers=default_headers).content

#addUser = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin/org/51a0dd22-bc5c-403f-971f-fd6270a9972b/users")

#xml_to_send = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><User xmlns=\"http://www.vmware.com/vcloud/v1.5\" name=\"createViaApiUser2\" >  <FullName>Example User Full Name</FullName> <EmailAddress>user@example.com</EmailAddress> <IsEnabled>true</IsEnabled> <Role href=\"https://vcd.lab.ord1.pc.rackspace.com/api/admin/role/ae910740-cbde-34ae-9d84-ef5c53880afe\" /> <Password>Pa55w0rd</Password> <GroupReferences /></User>"

#print addUser.execute_post(default_headers, xml_to_send).content


catalog = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/catalog/34c081f1-c5d2-4bea-a6fd-e5df8aab6ae1")

print "****2"
print catalog.execute_get(headers=default_headers).content

ph_catalog = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/catalogItem/6de086c3-92e7-4fc6-8a4c-0b5972b73491")

print "****3"
print ph_catalog.execute_get(headers=default_headers).content

ph_catalog_down_link = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/vAppTemplate/vappTemplate-7a2e11df-a8cb-4b8f-9986-1cb06f2c28aa")

print "****4"
print ph_catalog_down_link.execute_get(default_headers).content

#addToCatalog = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/catalog/73326c56-9249-436c-86c7-69f820f5a11d/actions/upload")
#addToCatalog = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin/catalog/73326c56-9249-436c-86c7-69f820f5a11d")
addToCatalog = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/vdc/738d13b3-db12-44d4-a154-84704d1f0097/media")
default_headers['Content-Type'] = 'application/vnd.vmware.vcloud.media+xml'

xml_to_send = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Media xmlns=\"http://www.vmware.com/vcloud/v1.5\" name=\"ph_ubuntu_upload.iso\" size=\"139005952\" imageType=\"iso\"> <Description>Pete test iso image</Description> </Media>"

print "****5"
#print addToCatalog.execute_post(headers=default_headers, payload=xml_to_send).content

del default_headers['Content-Type']


#https://vcd.lab.ord1.pc.rackspace.com/transfer/8f113454-4a35-47dd-8ff8-e522c4435558/file
upload_media = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/transfer/8f113454-4a35-47dd-8ff8-e522c4435558/file")
default_headers['Content-length'] = '10000'
f = open("lupu-528.005.iso", "rb")

print "****5.5"
"""
with open("lupu-528.005.iso", "rb") as f:
    byteLocation = 0
    bytesToSend = f.read(10000)
    while bytesToSend != b"":
        print upload_media.execute_delete(headers=default_headers, payload=bytesToSend).content
        byteLocation += 10000
        f.seek(byteLocation)
        bytesToSend = f.read(10000)
        print "byte location : " + str(byteLocation)
"""
del default_headers['Content-length']


#vdc_get = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin/vdc/3070a938-f11d-4269-902b-eccbcba8b69d")
top_get = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/vdc/738d13b3-db12-44d4-a154-84704d1f0097")
print "****6  this one has all the add links"
print top_get.execute_get(default_headers).content

"""start_up_vapp = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/vdc/738d13b3-db12-44d4-a154-84704d1f0097/action/instantiateVAppTemplate")
xml_to_send = "<InstantiateVAppTemplateParams" \
            "   xmlns=\"http://www.vmware.com/vcloud/v1.5\"" \
            "   xmlns:ovf=\"http://schemas.dmtf.org/ovf/envelope/1\"" \
            "   name=\"PH-API-TESTING\"" \
            "   deploy=\"false\"" \
            "   powerOn=\"false\">" \
            "   <Description>Testing API</Description>" \
            "   <Source href=\"https://vcd.lab.ord1.pc.rackspace.com/api/vAppTemplate/vappTemplate-7a2e11df-a8cb-4b8f-9986-1cb06f2c28aa\" />" \
            "</InstantiateVAppTemplateParams>"


print "****7"
default_headers['Content-Type'] = "application/vnd.vmware.vcloud.instantiateVAppTemplateParams+xml"
print start_up_vapp.execute_post(headers=default_headers, payload=xml_to_send).content
del default_headers['Content-Type']
"""

#vm_extension_get = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin/vdc/738d13b3-db12-44d4-a154-84704d1f0097")
vm_extension_get = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/vApp/vapp-e5bcb47e-b0e4-4399-adbc-d21cc572c60c")

print "****8"
print vm_extension_get.execute_get(default_headers).content

#turn_on_vapp = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/vApp/vapp-e5bcb47e-b0e4-4399-adbc-d21cc572c60c/power/action/powerOn")
#print "****9"
#print turn_on_vapp.execute_post(headers=default_headers).content

check_vapp_task = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin/extension/settings/general")
print "****10"
print check_vapp_task.execute_get(headers=default_headers).content

#check_prerunning_task = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin/extension/blockingTask/fd3919af-8f5c-48ae-a22e-27db2171578c")
#print "****11"
#print check_prerunning_task.execute_get(headers=default_headers).content

#abort_blocking_task = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin/extension/blockingTask/fd3919af-8f5c-48ae-a22e-27db2171578c/action/abort")
#xml_to_send = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><BlockingTaskOperationParams xmlns=\"http://www.vmware.com/vcloud/extension/v1.5\" ><Message>Approved by system administrator.</Message></BlockingTaskOperationParams>"
#default_headers['Content-Type'] = "application/vnd.vmware.admin.blockingTaskOperationParams+xml"
#print "****12"
#print abort_blocking_task.execute_post(headers=default_headers, payload=xml_to_send).content
#del default_headers['Content-Type']

delete_session = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/sessions")
response = delete_session.execute_delete(headers=default_headers)
print "****delete session request"
print response
print response.content
