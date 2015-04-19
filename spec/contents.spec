==========================================
content-image 			css 	.medium-4.columns a img
content-header  		css 	.medium-4.columns h2
content-desc    		css     .medium-4.columns p:nth-of-type(1)
content-more-button     css     .medium-4.columns p:nth-of-type(2) a
==========================================

@all
-------------------------

content-header
  below: content-image
  above: content-desc

content-desc
  below: content-header
  above: content-more-button

content-more-button
  below: content-header
  aligned vertically left:content-desc