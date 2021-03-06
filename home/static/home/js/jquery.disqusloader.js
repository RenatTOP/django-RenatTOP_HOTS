/*
	disqusLoader.js v1.0
	A JavaScript plugin for lazy-loading Disqus comments widget.
	-
	By Osvaldas Valutis, www.osvaldas.info
	Available for use under the MIT License
*/
!function(t,e,s,a){"use strict";var d,o,i,r,n=t(e),u=!1,l=!1,c=!1,f=!1,h="unloaded",p=t(),g=function(){if(!p.length||"loaded"==p.data("disqusLoaderStatus"))return!0;var s=n.scrollTop();if(p.offset().top-s>n.height()*l||s-p.offset().top-p.outerHeight()-n.height()*l>0)return!0;t("#disqus_thread").removeAttr("id"),p.attr("id","disqus_thread").data("disqusLoaderStatus","loaded"),"loaded"==h?DISQUS.reset({reload:!0,config:c}):(e.disqus_config=c,"unloaded"==h&&(h="loading",t.ajax({url:f,async:!0,cache:!0,dataType:"script",success:function(){h="loaded"}})))};n.on("scroll resize",(d=u,o=g,function(){var t=this,e=arguments,s=+new Date;i&&s<i+d?(clearTimeout(r),r=setTimeout(function(){i=s,o.apply(t,e)},d)):(i=s,o.apply(t,e))})),t.disqusLoader=function(e,s){s=t.extend({},{laziness:1,throttle:250,scriptUrl:!1,disqusConfig:!1},s),l=s.laziness+1,u=s.throttle,c=s.disqusConfig,f=!1===f?s.scriptUrl:f,(p=("string"==typeof e?t(e):e).eq(0)).data("disqusLoaderStatus","unloaded"),g()}}(jQuery,window,document);