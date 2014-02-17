from vclouddirector.action.client import ActionClient
from vclouddirector.session.behaviors import SessionBehaviors
from vclouddirector.model.org import Org


sb = SessionBehaviors(url="https://sample/api")
auth_token = sb.authenticate(user="test", org="test", password="test")

default_headers = {'accept': 'application/*+xml;version=1.5', 'x-vcloud-authorization': auth_token}

org = ActionClient(url="https://sample/org")

response = org.execute_get(headers=default_headers)

#print response.content

org1 = ActionClient(url="https://sample/api/org/51a0dd22-bc5c-403f-971f-fd6270a9972b")

response = org1.execute_get(headers=default_headers)

#print response.content

#roleRetrieve = ActionClient(url="https://vcd.lab.ord1.pc.rackspace.com/api/admin")
#print roleRetrieve.execute_get(headers=default_headers).content

addUser = ActionClient(url="https://sampleapi/admin/org/51a0dd22-bc5c-403f-971f-fd6270a9972b/users")

xml_to_send = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><User xmlns=\"http://www.vmware.com/vcloud/v1.5\" name=\"createViaApiUser2\" >  <FullName>Example User Full Name</FullName> <EmailAddress>user@example.com</EmailAddress> <IsEnabled>true</IsEnabled> <Role href=\"https://vcd.lab.ord1.pc.rackspace.com/api/admin/role/ae910740-cbde-34ae-9d84-ef5c53880afe\" /> <Password>Pa55w0rd</Password> <GroupReferences /></User>"

#print addUser.execute_post(default_headers, xml_to_send).content



