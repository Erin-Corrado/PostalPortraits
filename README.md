PostalPortraits
===============
A project formed in HackRU by:

* Nikhil Kumar
* Erin Corrado

Won an award for the best use of Context.io api 

Analyzes the content of a conversation thread on a users email and then
transfers those changes through image modifations using the Pillow image
manipulation tool.

Warning: the keys in this program are no longer working. If you would like
to use this program please register for your own keys

## Modules needed 

### Python Pacakges
<pre>
* requests
* rauth
* pillow
</pre>

To install python2 packages you need to run pip.
For example to install requests, you need to run:

<pre><code>pip install requests</code></pre>



### Inline Context.io module
An inline python module has been included in this repository. However, if you
would like to download the module yourself you can find it at:
<pre>http://www.context.io/</pre>

### Optional AlchemyApi module
If you would like to modify the code and prefer to use inline Alchemy module
over the direct GET request, then you can download the python module at:
<pre>http://www.alchemyapi.com/</pre>

## Sample Run

#### Before

![Before Image](huskybefore.jpg "Before Image")





#### After

![After Image](huskyafter.jpg "After Image")


## Image Manipulation

The mood/tone of the conversation is reflected through the overlayed color of the image. More red for more positive feelings, and more blue for negative feelings.
The length of the conversation and messages corresponds to the image's Gaussian blur. The longer the average message, the greater the blur.
The ratio of keywords to total words is used to determine the luminosity of the image. The more keywords, the brighter the image. The more noise words, the more contrast there is in the image.

