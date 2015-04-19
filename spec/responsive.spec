#Galen Demo

=====================================
header 				css #navigation .top-bar
left-menu			css .top-bar-section .left
right-menu		    css .top-bar-section .right
backstretch         css .backstretch

main-menu-items-*   xpath //section[@class='top-bar-section']/ul[@class='right']/li/a/parent::li

navigation-list     css .menu-icon
name 				css .name h1 a
contents-*			css .medium-4.columns

=====================================


@all
---------------------------
header
  inside: screen 0px top
  width: 100 % of screen/width

backstretch
  width: 100 % of screen/width  


@desktop
---------------------------
right-menu
  inside: header 0 px top right
  right of:left-menu
  contains: main-menu-items-*

left-menu
  inside: header 0 px top left
  left of:right-menu

navigation-list
  absent

backstretch
  height: ~ 15 % of screen/height

[1 - ${count("contents-*") - 1}]
contents-@
  aligned horizontally top:contents-@{+1}


#[1]
#main-menu-items-@
#  near: main-menu-item-@{+2} 0px left
#  aligned horizontally: main-menu-item-@{+2}


@mobile,tablet
---------------------------    
right-menu
  absent

left-menu
  absent

navigation-list
  visible
  inside:header 9 px top 
  inside:header 0 px right


@mobile
------------------------------
name
  visible
  text is: Feeling Responsive

backstretch
  height: ~ 8 % of screen/height  

[1 - ${count("contents-*") - 1}]
contents-@
  aligned vertically left:contents-@{+1}  

@tablet
------------------------------
name 
  absent

backstretch
  height: ~ 13 % of screen/height  

[1 - ${count("contents-*") - 1}]
contents-@
  aligned horizontally top:contents-@{+1}


