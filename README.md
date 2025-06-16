Steps :  


ISSUE : enchant hunspell.dll  module not found (issue in msix installed exe )  However the dll file is physically present.

Get the msi  from  https://drive.google.com/drive/folders/1cycZCUT8UBHhXUKJAy9OYqSZzdjm9E1J?usp=sharing
or else create an new msi  and create an msix 

Msix Creation steps :

1. Install the MSIX Packaging Tool 

Open Microsoft Store 

Search for MSIX Packaging Tool 

Click Install 

 

2. Launch the MSIX Packaging Tool 

Run MSIX Packaging Tool as Administrator 

3. Start New Package 

Click "Application package" 

Select "Create a package on this computer" 

Click Next 

Then again Click next 

4. Provide Installer Information 

Installer Location: Browse to your .msi file 

Choose  sing with a certificate  (.pfx)   (guide below)

Browse your pfx certificate  and enter its password  (it can be MyPassword123) 

Click Next 

5. Choose Package Information 

Fill out the information (If already added just change publisher to CN=”Zendalona”) 

Click Next 

IF done Properly Installation Should be Started 

After Installation Click Next in Msix Packaging tool 

Click next  >  Click on “Yes Move on” >Next  >Create  

Msix Should be created 



run the msix it should give that error



Sing certificate guide 
Steps: 

 
Step 1: Open PowerShell as Administrator 

Press Start 

Type PowerShell 

Right-click → Run as Administrator 

Step 2: Create a Self-Signed Certificate 

Copy and paste this into PowerShell: 

$cert = New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=Zendalona" -CertStoreLocation "Cert:\LocalMachine\My" 
 
Step 3: Export the Certificate as a .pfx File 
 
This creates a file called ZendalonaCert.pfx on your Desktop, protected with password MyPassword123. 
  
$pwd = ConvertTo-SecureString -String "MyPassword123" -Force -AsPlainText 

$pfxPath = "$env:USERPROFILE\Desktop\ZendalonaCert.pfx" 

Export-PfxCertificate -Cert $cert -FilePath $pfxPath -Password $pwd 
 
Step 4: Also Export a .cer File (To Trust It Later) 

$cerPath = "$env:USERPROFILE\Desktop\ZendalonaCert.cer" 
Export-Certificate -Cert $cert -FilePath $cerPath 
 

This will save a .cer file on your Desktop for trust installation. 

 
 
 Step 5: Trust the Certificate on Your System 

Double-click ZendalonaCert.cer on Desktop 

Click Install Certificate 

Select Local Machine → Next 

Choose Place all certificates in the following store 

Click Browse 

Choose Trusted Root Certification Authorities 

Finish the wizard and accept any warning 
