$("#nav").affix({offset:{top:$("header").height()}}),$("#side-nav").affix({offset:{top:200}});var $body=$(document.body),navHeight=$(".navbar").outerHeight(!0)+10;$body.scrollspy({target:"#side-nav",offset:navHeight}),$(".scroller").click(function(){if(location.pathname.replace(/^\//,"")==this.pathname.replace(/^\//,"")&&location.hostname==this.hostname){var a=$(this.hash);if(a=a.length?a:$("[name="+this.hash.slice(1)+"]"),a.length)return $("html,body").animate({scrollTop:a.offset().top-50},1e3),!1}});