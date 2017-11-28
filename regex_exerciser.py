import json
import re
import time


print('Loading function')


def task(code):
    rep = 1000
    pattern = '<div([^>]+)>'
    ini = time.time()
    for i in range(rep):
        results = re.findall(pattern, code)

    message = "{0} Repetitions. Avg = {1:.3f} ms".format(rep, (time.time()-ini)*1000/rep)
    print(message)


def lambda_handler(event, context):
    task(code*2)
    return {
        "isBase64Encoded": "false",
        "statusCode": 200,
        "headers": {"headerName": "headerValue"},
        "body": "alfredo"
    }


code = """\
<!-- html-header type=current begin -->

	<!DOCTYPE html>


	<html lang="en">
	<head>
	<!-- Render IE9 -->
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">



<script>
(function (s,o,n,a,r,i,z,e) {s['StackSonarObject']=r;s[r]=s[r]||function(){
 (s[r].q=s[r].q||[]).push(arguments)},s[r].l=1*new Date();i=o.createElement(n),
 z=o.getElementsByTagName(n)[0];i.async=1;i.src=a;z.parentNode.insertBefore(i,z)
 })(window,document,'script','https://www.stack-sonar.com/ping.js','stackSonar');
 stackSonar('stack-connect', '66');
</script>

	<script id="before-content" type="text/javascript">
(function () {
    if (typeof window.sdmedia !== 'object') {
         window.sdmedia = {};
    }
    if (typeof window.sdmedia.site !== 'object') {
        window.sdmedia.site = {};
    }

    var site = window.sdmedia.site;
    site.rootdir = "//slashdot.org";
}());

var pageload = {
	pagemark: '318981028117954988',
	before_content: (new Date).getTime()
};
function pageload_done( $, console, maybe ){
	pageload.after_readycode	= (new Date).getTime();
	pageload.content_ready_time	= pageload.content_ready - pageload.before_content;
	pageload.script_ready_time	= pageload.after_readycode - pageload.content_ready;
	pageload.ready_time		= pageload.after_readycode - pageload.before_content;
	// Only report 1% of cases.
	maybe || (Math.random()>0.01) || $.ajax({ data: {
		op: 'page_profile',
		pagemark: pageload.pagemark,
		dom: pageload.content_ready_time,
		js: pageload.script_ready_time
	} });
}
</script>
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

		<title>Slashdot: News for nerds, stuff that matters</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

		<meta name="description" content="Slashdot: News for nerds, stuff that matters. Timely news source for technology related news with a heavy slant towards Linux and Open Source issues.">

		<meta property="og:title" content="Slashdot: News for nerds, stuff that matters">
		<meta property="og:description" content="Slashdot: News for nerds, stuff that matters. Timely news source for technology related news with a heavy slant towards Linux and Open Source issues.">



		<meta property="fb:admins" content="100000696822412">
		<meta property="fb:page_id" content="267995220856">

		<meta name="viewport" content="width=1000, user-scalable=yes, minimum-scale=0, maximum-scale=10.0" />
		<meta name="apple-mobile-web-app-capable" content="yes">
		<meta name="apple-mobile-web-app-status-bar-style" content="black">

		<link rel="canonical" href="https://slashdot.org">

		<link rel="alternate" media="only screen and (max-width: 640px)" href="http://m.slashdot.org" >


		<link rel="stylesheet" type="text/css" media="screen, projection" href="//a.fsdn.com/sd/classic.css?acf4e08ef95906a6" >
		<!--[if IE 8]><link rel="stylesheet" type="text/css" media="screen, projection" href="//a.fsdn.com/sd/ie8-classic.css?acf4e08ef95906a6" ><![endif]-->
		<!--[if IE 7]><link rel="stylesheet" type="text/css" media="screen, projection" href="//a.fsdn.com/sd/ie7-classic.css?acf4e08ef95906a6" ><![endif]-->







	<!--  -->





	<!-- SMACKS: NEW CSS -->
	<link rel="stylesheet" href="//a.fsdn.com/sd/css/app.css?acf4e08ef95906a6">

	<script type='text/javascript'>
var _gaq = _gaq || [];
</script>









<script type="text/javascript" id="pbjs_script" data-dom="https://d3tglifpd8whs6.cloudfront.net"  src="https://d3tglifpd8whs6.cloudfront.net/js/prebid/slash-homepage/slash-homepage.min.js"></script>
<script type='text/javascript'>
    /*global performance */
    var googletag = window.googletag || {};
    googletag.cmd = googletag.cmd || [];
</script>

<!-- prep GPT ads -->
<script type='text/javascript'>
(function() {
	function page_type (loc) {
		/*
		only four page types:
		- Story
		- Poll
		- Homepage (/ only)
		- Other (but AdOps wants 'Homepage' again)
		*/
		var path = loc.pathname;
		var just_the_root = /^\/?$/.test(path);
		var story_or_poll = /^\/(story(?=\/)|submission(?=\/)|poll(?=\/|Booth|s\b))/i.exec(path);

		var page_type = just_the_root ? 'homepage'
		              : story_or_poll ? story_or_poll[1]
		              :                 'other'

		// exceptions
		if (page_type.toLowerCase() === 'submission')
			page_type = 'story'; // submissions are like stories, right?
		else if (page_type.toLowerCase() === 'other')
			page_type = 'homepage'; // this one might move out of here

		return page_type;
	}
	function page_section (loc) {
		var greek = ['alpha', 'beta', 'gamma', 'delta'].join('|');
		var hostwise = '^([a-z]+)(?:-(?:'+greek+'))?\\.(?:slashdot\\.org|[a-z]+-[0-9]+\\.sb\\.sf\\.net)$';
		var pathwise = '^/(?:(recent|popular|blog)|stories/([^/]+))';
		var rootwise = '^\/?$';

		var hostwisely = new RegExp(hostwise,'i').exec(loc.hostname);
		var pathwisely = new RegExp(pathwise,'i').exec(loc.pathname);
		var rootwisely = new RegExp(rootwise,'i').exec(loc.pathname);

		var section = (rootwisely && 'homepage')
		           || (pathwisely && (pathwisely[1] || pathwisely[2]))
		           || ''
		            ;

                section.replace(/[^_a-z]/ig, '');

		return section;
	}
	function single_size (size) {
		return '' + size[0] + 'x' + size[1];
	}
	function sz_sz (sz) {
		var str = '';
		var sizes = [];
		if (sz[0] instanceof Array) {
			for (size in sz) {
				sizes.push(single_size(sz[size]));
			}
			return sizes.join(',');
		} else {
			return single_size(sz);
		}
	}

	function merge_tpc_array_to_str(array1,array2) {
		var tpc_final = array1.concat(array2);
		var uniq = tpc_final.reduce(function(a,b){
		if (a.indexOf(b) < 0 ) a.push(b);
			return a;
		},[]);

		var tpc_str = uniq.join(',');
		tpc_str = tpc_str.replace(/[^_a-z,]/ig, '');
		tpc_str = tpc_str.replace(/^,/ig, '');
		return tpc_str;
	}

	/* LEGEND:
		- 'sz' = "size"
		- 'npt' = "no page type" in ad unit name
	*/
	var tags = {
        '728x90_A': { 'sz': [[728, 90], [970, 90], [970, 250], [980, 66]] },
        '728x90_B': { 'sz': [728, 90] },
        '728x90_C': { 'sz': [728, 90], 'skip': { 'homepage': 1 } },
        'HubIcon_200x90_A': { 'sz': [[200, 90], [220, 90]]},
        'PowerSwitch_980x66_A': { 'sz': [980, 66], 'skip': { 'homepage': 1 } },
        'PollPeel': { 'sz': [200, 90], 'skip': { 'homepage': 1 } },
        //'VideoWidget_300x250': { 'sz': [300, 250], 'npt': 1 },
        '300x250_A': { 'sz': [[300, 250], [300, 600], [300, 1050]] },
        '300x250_B': { 'sz': [[300, 250], [300, 600]] },
        '300x250_C': { 'sz': [[300, 250], [300, 600]] },
        '300x250_D': { 'sz': [[300, 250], [300, 600]] },
        'Pulse_300x600_A': { 'sz': [300, 600] },
        //'Polls_Detail_300x250_A': { 'sz': [[300, 250], [300, 600]], 'npt': 1 },
        //'Poll_300x250_A': { 'sz': [[300, 250], [300, 600]], 'npt': 1 },
        //'SD_Story_1x1': { 'sz': [1, 1] },
        '1x1': { 'sz': [1, 1] }
	};

	//var network_path = '/41014381/Slashdot/';
	var network_path = '/41014381/Slashdot/';
	var tag_name_prefix = 'SD';
	var tag_name_linkage = '_';
	var tag_name_pagetype = page_type(location);
	var tag_topic = page_section(location);
    if(tag_name_pagetype == 'poll'){
        tag_name_pagetype = 'Poll';
    }
	var before_tag_pagetyped    = network_path
	                            + tag_name_prefix
	                            + tag_name_linkage
	                            + tag_name_pagetype
	                            + tag_name_linkage
	                            ;
	var before_tag_pagetypeless = network_path
	                            + tag_name_prefix
	                            + tag_name_linkage
	                         /* + tag_name_pagetype */
	                         /* + tag_name_linkage */
	                            ;


	googletag.cmd.push(function() {

	    function remove_sticky_top() {
	        setTimeout(function(){
	            $('#div-gpt-ad-728x90_a').parent('div').addClass('adwrap-viewed-banner');
               $('#div-gpt-ad-728x90_a').addClass('viewableImpression');
            }, 1000);

	    }
	    function remove_sticky_railad() {
	        setTimeout(function(){
                $('#slashboxes .adwrap-unviewed').addClass('adwrap-viewed-railad');
                $('.railad').addClass('viewableImpression');
            }, 1000);
	    }
		function viewable_imp (slot) {
	        for(var i in slot) {
	            if(typeof slot[i] !== 'string') continue;
	            switch(slot[i]){
                  case "/41014381/Slashdot/SD_homepage_728x90_A":
                  case "/41014381/Slashdot/SD_story_728x90_A":
                  case "/41014381/Slashdot/SD_Poll_728x90_A":
                  case "/41014381/Slashdot/SD_homepage_728x90_Ref_A":
                  case "/41014381/Slashdot/SD_story_728x90_Ref_A":
                  case "/41014381/Slashdot/SD_Poll_728x90_Ref_A":
	                    remove_sticky_top();
	                    break;
                  case "/41014381/Slashdot/SD_homepage_300x250_A":
                  case "/41014381/Slashdot/SD_story_300x250_A":
                  case "/41014381/Slashdot/SD_Poll_300x250_A":
                  case "/41014381/Slashdot/SD_homepage_300x250_Ref_A":
                  case "/41014381/Slashdot/SD_story_300x250_Ref_A":
                  case "/41014381/Slashdot/SD_Poll_300x250_Ref_A":
	                    remove_sticky_railad();
	                    break;
	            }
	            //if(slot[i] === "/41014381/Slashdot/SD_homepage_728x90_A") remove_sticky_top();
	            //if(slot[i] === "/41014381/Slashdot/SD_homepage_300x250_A") remove_sticky_railad();
	        }
		}
		function define_me_a_slot (tag) {
			if (tags[tag].skip && tags[tag].skip[tag_name_pagetype])
				return;
			var sandbox_regex = /[0-9]\.xb\.sf\.net$/i;
			var full_name = tags[tag].npt  // "no page type"
			              ? before_tag_pagetypeless + tag
			              : before_tag_pagetyped    + tag
			              ;
			var div_id = 'div-gpt-ad-' + tag.toLowerCase();

			var service;
            // extend jQuery and get URL query params
            jQuery.extend({
              getQueryParameters : function(str) {
            	  return (str || document.location.search).replace(/(^\?)/,'').split("&").map(function(n){
                  return n = n.split("="),this[n[0]] = n[1],this
                  }.bind({}))[0];
              }
            });

            var queryParams = $.getQueryParameters();

            if( queryParams.source === 'autorefresh' ) {
                full_name = full_name.replace(/(\d+x\d+)/,'$1_Ref');
                //console.log('TAG NAME: ', full_name);
            }

			service = googletag.defineSlot(
				  full_name
				, tags[tag].sz
				, div_id
			).addService(googletag.pubads());

			service.setTargeting('sz', tags[tag].sz);


			var frontend_tpc = tag_topic.split(",");
			var backend_tpc = [  ];

			var tpc_final = merge_tpc_array_to_str(frontend_tpc,backend_tpc);

			service.setTargeting('tpc', tpc_final);
			if (location.hostname.match(sandbox_regex)) {
				service.setTargeting('test', 'adops');
			}

		}

		for (tag in tags) {
			define_me_a_slot(tag, false);
		}
		googletag.pubads().addEventListener('impressionViewable', function(event) {
			viewable_imp(event.slot);
		    });

                googletag.pubads().setTargeting('requestSource', 'GPT');
		googletag.pubads().enableAsyncRendering();


		googletag.pubads().collapseEmptyDivs();
		window.bizxPrebid.SAFEFRAMES = true;
		bizxPrebid.Ads.pushToGoogle();
		googletag.enableServices();
	});
})();
</script>



<!-- CrossPixel -->
<script type="text/javascript"> try{(function(){ var cb = new Date().getTime(); var s = document.createElement("script"); s.defer = true; s.src = "//tag.crsspxl.com/s1.js?d=2397&cb="+cb; var s0 = document.getElementsByTagName('script')[0]; s0.parentNode.insertBefore(s, s0); })();}catch(e){} </script>

<!-- AdBlock Check -->
<script>
var isAdBlockActive = true;
</script>
<script async src="//a.fsdn.com/sd/js/scripts/ad.js?acf4e08ef95906a6"></script>

</head>
<body class="anon index2 ">


	<script src="//a.fsdn.com/sd/all-minified.js?acf4e08ef95906a6" type="text/javascript"></script>


	<script type="text/javascript">
(function(){
var regexp=/\s*(?:\d+|many)\s+more\s*/i;


	var auto_more_count = 1;

	function auto_more(){
		var $more_link = $('#more-experiment a');
		$more_link.each(function(){
			var $lastitem = $('#firehoselist>article.fhitem:visible:last');
			if ( Bounds.intersect(window, $lastitem) ) {


				!--auto_more_count && (auto_more=undefined);
				// don't allow a call till the next paginate gets built and |more_possible|
				$(document).unbind('scroll', call_auto_more);
			}
		});
	};

	function call_auto_more(){ auto_more && auto_more(); }


$('#more-experiment a').
	live('more-possible', function( event ){
		var $more_link=$(this);
		if ( regexp.test($more_link.text()) ) {

			$(document).bind('scroll', call_auto_more);
		} else {
			$(document).unbind('scroll', call_auto_more);

		}
	});
})();
</script>
	<!--[if lt IE 9]><script src="//a.fsdn.com/sd/html5.js"></script><![endif]-->


	<script type="text/javascript">
		(function() {
			if (typeof window.janrain !== 'object') window.janrain = {};
			if (typeof window.janrain.settings !== 'object') window.janrain.settings = {};

			/* _______________ can edit below this line _______________ */

			janrain.settings.tokenUrl = 'https://slashdot.org/token_callback.pl';
			janrain.settings.type = 'embed';
			janrain.settings.appId = 'ggidemlconlmjciiohla';
			janrain.settings.appUrl = 'https://login.slashdot.org';
			janrain.settings.providers = [
			'googleplus',
			'facebook',
			'twitter',
			'linkedin'];
			janrain.settings.providersPerPage = '5';
			janrain.settings.format = 'one column';
			janrain.settings.actionText = 'Sign in with';
			janrain.settings.showAttribution = false;
			janrain.settings.fontColor = '#666666';
			janrain.settings.fontFamily = 'lucida grande, Helvetica, Verdana, sans-serif';
			janrain.settings.backgroundColor = '#ffffff';
			janrain.settings.width = '300';
			janrain.settings.borderColor = '#cccccc';
			janrain.settings.borderRadius = '5';    janrain.settings.buttonBorderColor = '#CCCCCC';
			janrain.settings.buttonBorderRadius = '0';
			janrain.settings.buttonBackgroundStyle = 'gray';
			janrain.settings.language = '';
			janrain.settings.linkClass = 'janrainEngage';

			/* _______________ can edit above this line _______________ */

			function isReady() { janrain.ready = true; };
			if (document.addEventListener) {
			  document.addEventListener("DOMContentLoaded", isReady, false);
			} else {
			  window.attachEvent('onload', isReady);
			}

			var e = document.createElement('script');
			e.type = 'text/javascript';
			e.id = 'janrainAuthWidget';

			e.src = 'https://rpxnow.com/js/lib/login.slashdot.org/engage.js';

			var s = document.getElementsByTagName('script')[0];
			s.parentNode.insertBefore(e, s);
		})();
	</script>

		<script src="//cdn-social.janrain.com/social/janrain-social.min.js"></script>
		<script type="text/javascript">
			(function($) {
				$(function(){
					janrain.settings.appUrl = "https://login.slashdot.org";
					$twitter = $('body .janrain_twitterButton');
					$twitter.append('<i class="icon-twitter"></i>');

					janrain.settings.social = {
						providers: [
							"facebook",
							"twitter",
							"linkedin",
							"native-googleplus",
							"native-reddit"
						],
						shareCountMin: "100",
						shareCountMode: "combined"
					};
				});
			})($j);
		</script>
	<!-- index2_variant |A|-->

	<!-- TABOOLA -->
	<script type="text/javascript">
	  window._taboola = window._taboola || [];
	  _taboola.push({home:'auto'});
	  !function (e, f, u) {
		e.async = 1;
		e.src = u;
		f.parentNode.insertBefore(e, f);
	  }(document.createElement('script'),
	  document.getElementsByTagName('script')[0],
	  '//cdn.taboola.com/libtrc/slashdot/loader.js');
	</script>

	<!-- html-header type=current end --><!-- header type=current begin -->



	<link rel="top"       title="News for nerds, stuff that matters" href="//slashdot.org/" >
<link rel="search"    title="Search Slashdot" href="//slashdot.org/search.pl">
<link rel="alternate" title="Slashdot RSS" href="http://rss.slashdot.org/Slashdot/slashdotMain" type="application/rss+xml">
	<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">


		<div id="top_parent"></div>
		<a name="topothepage"></a>

		<div class="container">
			<div class="nav-wrap">
				<nav class="nav-primary" role="navigation" aria-label="Global Navigation">
					<h1 class="logo">
	<a href="//slashdot.org"><span>Slashdot</span></a>
</h1>

<ul class="nav-site">
	<li><a href="//slashdot.org"><i class="icon-book" title="Stories"></i><span>Stories</span></a></li>
	<li>
		<ul class="filter-firehose">
			<li class="nav-label">Firehose <i class="icon-angle-right"></i></li>
			<li><a href="//slashdot.org/recent">All</a></li>
			<li><a href="//slashdot.org/popular">Popular</a></li>
		</ul>
	</li>
	<li><a href="//slashdot.org/polls"><i class="icon-chart-bar" title="Polls"></i><span>Polls</span></a></li>

	<!--
	<li><a href="//ask.slashdot.org"><i class="icon-question-circle"></i><span>Ask</span></a></li>

	<li><a href="//events.slashdot.org"><i class="icon-calendar"></i><span>Events</span></a></li>
	-->
	<li><a href="http://deals.slashdot.org/?utm_source=slashdot&amp;utm_medium=navbar&amp;utm_campaign=dealshp_1" target="_blank"><i class="sd-mini" title="Deals"></i> <span>Deals</span></a></li>
</ul>
<a href="//slashdot.org/submission" class="btn btn-success">Submit</a>
				</nav>
				<nav class="nav-user" role="navigation" aria-label="user access and account controls">
					<form id="search" class="form-inline nav-search-form" method="get" action="//slashdot.org/index2.pl">
<!-- //slashdot.org/index2.pl" -->
	<div class="form-group">
		<label class="sr-only" for="sitesearch">Search Slashdot</label>
		<div class="input-group">
			<input type="text" id="" class="" name="fhfilter" value="" placeholder="Search">
		</div>
	</div>
	<button type="submit" class="btn icon-search"></button>
</form>
<ul class="user-access">


			<li >
				<a href="//slashdot.org/my/login"  onclick="show_login_box(); return false;"><i class="icon-login"></i><span> Login</span></a>

			</li>



			<li class="nav-label">or</li>



			<li >
				<a href="//slashdot.org/my/newuser"  onclick="getModalPrefs('newUserModal', 'Create Account', 1); $('#modal_box').addClass('join'); return false;"><i class="icon-user-add"></i><span> Sign up</span></a>

			</li>


</ul>
				</nav>
			</div>
			<div class="nav-secondary-wrap">
				<nav class="nav-secondary" role="secondary-navigation">
	<ul>
		<li class="nav-label">Topics: </li>
		<li><a href="//devices.slashdot.org">Devices</a></li>
		<li><a href="//build.slashdot.org">Build</a></li>
		<li><a href="//entertainment.slashdot.org">Entertainment</a></li>
		<li><a href="//technology.slashdot.org">Technology</a></li>
		<li><a href="//slashdot.org/?fhfilter=opensource">Open Source</a></li>
		<li><a href="//science.slashdot.org">Science</a></li>
		<li><a href="//yro.slashdot.org">YRO</a></li>
		<!-- <li><a href="//slashdot.org/topics.pl">more...</a></li> -->
	</ul>
</nav>
<nav class="nav-social" role="social navigation">
	<ul>
		<li class="nav-label">Follow us:</li>
		<li><a href="http://rss.slashdot.org/Slashdot/slashdotMain" target="_blank"><i class="icon-rss-squared"></i><span class="sr-only">RSS</span></a></li>
		<li><a href="http://www.facebook.com/slashdot" target="_blank"><i class="icon-facebook-squared"></i><span class="sr-only">Facebook</span></a></li>
		<li><a href="https://plus.google.com/112601993642376762846/" target="_blank"><i class="icon-gplus-squared"></i><span class="sr-only">Google+</span></a></li>
		<li><a href="http://twitter.com/slashdot" target="_blank"><i class="icon-twitter-squared"></i><span class="sr-only">Twitter</span></a></li>
		<li><a href="//slashdot.org/newsletter" target="_blank"><i class="icon-mail-squared"></i><span class="sr-only">Newsletter</span></a></li>
	</ul>
</nav>
			</div>
		</div>

		<section>

			<div class="message-bar" id="firehose-message-tray">
				<span class="icon-quote-left"></span>
				<p>


						Follow Slashdot stories on <a href="http://twitter.com/slashdot">Twitter</a>

				</p>
			</div>


			<div id='embbeded_login_modal' class="hide">
<form action="https://slashdot.org/my/login" method="post" onsubmit="if (global_returnto) { this.returnto.value = global_returnto }" class="embedded"><fieldset style="-webkit-border-radius:10px 10px 0 0;border-radius:10px 10px 0 0;-moz-border-radius:10px 10px 0 0">
<div style='height:25px;'>&nbsp;</div>
    <input type="hidden" name="returnto" value="">
    <input type="hidden" name="op" value="userlogin">
    <p>
        <label class="fleft" for="unickname">Nickname:</label>
        <input type="text" name="unickname" value="">
    </p>
    <p>
        <label class="fleft" for="upasswd">Password:</label>
        <input type="password" name="upasswd" placeholder="6-1024 characters long">
    </p>
    <label class="checkbox"><input type="checkbox" name="login_temp" value="yes"> Public Terminal</label>
    <br>
    <hr>
    <input type="submit" name="userlogin" value="Log In" class="fno"> <a href="//slashdot.org/my/mailpassword" class="btn link" onclick="getModalPrefs('sendPasswdModal', 'Retrieve Password', 1); return false;">Forgot your password?</a>
</fieldset></form>

<div id="janrainEngageEmbed"></div>
<div class="actions">
 <a class="ico close" onclick="hide_login_slider();" href=""><span>Close</span></a>
</div>
</div>


			<div class="banner-wrapper">
				<div class="adwrap adwrap-unviewed banner-contain">

					<div id='div-gpt-ad-728x90_a'><script type='text/javascript'>
googletag.cmd.push(function(){
googletag.display('div-gpt-ad-728x90_a');});</script></div>
					<div id='div-gpt-ad-hubicon_200x90_a'><script type='text/javascript'>
googletag.cmd.push(function(){
googletag.display('div-gpt-ad-hubicon_200x90_a');});</script></div>
				</div>
			</div>

		<a name="main-articles"></a>

	<!-- header type=current end --><!--body begin -->








	<style type="text/css">
menu, menu * {
	text-decoration:none;
}

menu[type=context] {
	display:none;
	position:absolute;
	z-index:10000;
}

menu[type=context]:not(.brief) {
	background-color:#dfdfdf;
	margin:0;
	padding:2px 0.5em;
	border-style:solid;
	border-width:1px;
	border-color:#eeeeee #aaaaaa #aaaaaa #eeeeee;
	-moz-border-radius-topright:.7em;
	-webkit-border-top-right-radius: 0.7em 0.7em;
}

menu.full[type=context] > a.slash-hover:first-child {
	-moz-border-radius-topright:.6em;
	-webkit-border-top-right-radius: 0.6em 0.6em;
}



menu.brief[type=context] > a {
	-moz-border-radius:.6em;
	-webkit-border-radius: 0.6em;
	color:#ffffff;
	background-color:#000000;
}

/*
span.briefmenu a.tag:not(.datatype) {
    padding-left:.5em;
}
*/




/* #tag-menu a, #feedback-menu a  { */
menu.tag-menu-admin a {
	display:list-item;
	list-style:none;
	text-align:left;
	font-weight:bold;
	color:black;
	padding:0.1em 0.5em;
	margin:-0.1em -0.5em;
	cursor:pointer;
}


.tags .edit-bar { position:relative; }
article aside .share .addthis_toolbox { display:block; width:60px; float:left; }
article aside.view_mode .share { min-width:120px; padding-top:.5em; }
#firehose.list article header h2 {padding-left: 20px; !important}
.novote .vote { display:none; }

.vote > a, .votedup > a, .voteddown > a {
	display:inline-block;
	height:22px;
	width:22px;
	margin: 2px 10px 0 0;
	color:rgb(255,255,255);
	text-decoration:none;
	line-height:22px;
	text-align:center;
	font-weight:bold;
	font-size:14px;
	border-width:1px;
	border-style:solid;
	border-color:rgba(0,0,0,0.5);
}

.vote > a, .votedup > a, .voteddown > a {color:rgb(0,0,0);}

article.fhitem-submission h2 .vote > a, article.fhitem-submission h2 .votedup > a, article.fhitem-submission h2 .voteddown > a { border-color:rgba(0,0,0,0.15); }
.vote .up, .vote .down, .votedup .up, .votedup .down, .voteddown .up, .voteddown .down { border-radius: 4px; -moz-border-radius: 4px; -webkit-border-radius: 4px; /* text-shadow:0 0 2px #000000; }*/}
article:not(.fhitem-story) .vote .up,article:not(.fhitem-story) .vote .down,article:not(.fhitem-story) .votedup .up,article:not(.fhitem-story) .votedup .down,article:not(.fhitem-story) .voteddown .up,article:not(.fhitem-story) .voteddown .down { /*text-shadow:none !important; */}
.voteddown .down, .votedup .up { margin-right: 10px; text-indent:2px; line-height:24px; }
article:not(.fhitem-story) .votedup .up,article:not(.fhitem-story) .voteddown .down {background: rgb(174,174,174);background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(rgb(174,174,174)), to(rgb(193,193,193)));background-image: -moz-linear-gradient(100% 100% 90deg,rgb(193,193,193), rgb(174,174,174) 100%);color:rgb(0,0,0);}
article.fhitem-story .votedup .up,article.fhitem-story .voteddown .down {background: rgb(0,66,66);background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(rgb(0,53,53)), to(rgb(0,102,102)));background-image: -moz-linear-gradient(100% 100% 90deg,rgb(0,102,102), rgb(0,53,53) 100%);}




#tag-menu span.var-tag {
font-weight:normal;
color:#444444;
}

menu.reasons-menu a {
padding:0 .25em 0 .25em;
font-size:80%;
-moz-border-radius:.5em;
-webkit-border-radius:.5em;
cursor:pointer;
}

menu.reasons-menu a:hover {
background:rgb(153,153,153);
background:-moz-linear-gradient(100% 100% 90deg, rgb(102,102,102), rgb(153,153,153) 70%) repeat scroll 0 0 rgb(102,102,102);
background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(rgb(153,153,153)), to(rgb(102,102,102)));
color:#fff;
text-decoration:none;
font-weignt:normal;
}

article.fhitem-story menu.reasons-menu a:hover {
background:#002323 !important;
background:-moz-linear-gradient(100% 100% 90deg, #002323, #005353 70%) repeat scroll 0 0 #002323 !important;
background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#005353), to(#002323)) !important;
}


menu.reasons-menu {
	display:none;
	margin:0;
	padding:0;
}

div.fhitem h3 menu.reasons-menu {
margin:0.25em 0 0;
}

div.fhitem h3 menu.reasons-menu a.tag {
font-size:.8em;
}

#tag-menu a.slash-hover,
#feedback-menu a.slash-hover,

.tag-display span.tag:hover,
.tag-display span.tag.trigger {
	color:white;
	background-color:rgb(0, 85, 85);
}

#tag-menu a.slash-hover span.var-tag {
	color:#eee;
}

.tag-entry.default {
        color:#ccc;
}

.brief .nix {
	margin-top:-1.35em;
	margin-left:0px;
	margin-top:-1.15em;
	text-decoration:none;
	line-height:1.35em;
	padding:0 2px;
	-moz-border-radius:.6em 0 0 .6em;
	-webkit-border-radius:.6em 0 0 .6em;
	-o-border-radius:.6em 0 0 .6em;
	border-radius:.6em 0 0 .6em;
    color:#fff !important;
    background:transparent !important;
}

.brief .nix:hover {
    background:rgb(153,153,153) !important;
    background:-moz-linear-gradient(100% 100% 90deg, rgb(102,102,102), rgb(153,153,153) 70%) repeat scroll 0 0 rgb(102,102,102) !important;
    background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(rgb(153,153,153)), to(rgb(102,102,102))) !important;
}

</style>

<menu id="nix-reasons" style="display:none">
	<a class="tag">binspam</a><a class="tag">dupe</a><a class="tag">notthebest</a><a class="tag">offtopic</a><a class="tag">slownewsday</a><a class="tag">stale</a><a class="tag">stupid</a>
</menu>
<menu id="nod-reasons" style="display:none">
	<a class="tag">fresh</a><a class="tag">funny</a><a class="tag">insightful</a><a class="tag">interesting</a><a class="tag">maybe</a>
</menu>
<menu id="comment-nix-reasons" style="display:none">
	<a class="tag">offtopic</a><a class="tag">flamebait</a><a class="tag">troll</a><a class="tag">redundant</a><a class="tag">overrated</a>
</menu>
<menu id="comment-nod-reasons" style="display:none">
	<a class="tag">insightful</a><a class="tag">interesting</a><a class="tag">informative</a><a class="tag">funny</a><a class="tag">underrated</a>
</menu>

<menu id="tag-nod-reasons" style="display:none">
	<a class="tag">descriptive</a>
</menu>
<menu id="feedback-menu" class="tag-menu-admin" type="context">
	<a class="tag">typo</a><a class="tag">dupe</a><a class="tag">error</a>
</menu>
<menu id="tag-menu" class="tag-menu-admin none" type="context">

<!--	<a data-op="!" class="nix">!<span class="var-tag hide"></span></a>-->

</menu>

<script type="text/javascript">
$(function(){
var $CURRENT_MENU, $TAG_MENU=$('#tag-menu'), NOTNOT=/^!!/, IE7=/^7\.0/, TAG_PREFIX=/^\/tag\//;

function get_tag_name( $tag ){
	return ($tag.attr('href') || '').replace(TAG_PREFIX, '') || $tag.text().toLowerCase();
}

function trigger_menu( e, selector, $menu, menu_content ){
	var $target=$(original_target(e, selector)), in_use=$target.is('.trigger');
	if ( $CURRENT_MENU ) {
		$CURRENT_MENU.menu('cancel', e);
		$CURRENT_MENU = null;
	}

	if ( !in_use ) {
		menu_content && $menu.stop(true, true).hide().html(menu_content);
		($CURRENT_MENU=$menu).menu('context', e);
	}
	return !in_use;
}

function open_menu( trigger, $menu ){
	var $trigger=$(trigger), $fhitem=$trigger.closest('.fhitem');
	$fhitem.length && user_intent('interest', $fhitem[0]);

	$menu.appendTo(document.body).css({ opacity:0 }).show();

	var 	right	= $fhitem.offset().left + $fhitem.width(),
		global	= $trigger.offset(),
		local	= $menu.offsetParent().offset();

	// Ugly IE position hack required:
	$.browser.msie && IE7.test($.browser.version) && (local.top = 0);

	// pin the menu (horizontally) on-screen
	global.left = Math.min(global.left, right-$menu.width());

	$trigger.addClass('trigger');
	$menu.css({
		position:	'absolute',
		top:		global.top - local.top + $trigger.height(),
		left:		global.left - local.left,
		opacity:	1
	});
}

function close_menu( trigger, $menu ){
	$menu.hide();
	$(trigger).removeClass('trigger');
	($CURRENT_MENU===$menu) && ($CURRENT_MENU=false);
}

/* T2 tag context-menu */
var $TAG_MENU=$('#tag-menu'), NOTNOT=/^!!/;


    var user_is_admin = 0;



$('a[rel=tag]').live('mousedown',function(ea){
    window.open(this.href);
    return false;
})

$('.tag-bar .disagree').live('mousedown',function(ee){
	var fhitem = $(original_target(ee)).closest('.fhitem')[0],
		command = ('!' + $(original_target(ee)).attr("data-tag")).replace(NOTNOT, '');
    try { Tags.submit(fhitem, command); } catch ( err ) {  }
    return false;
})



$('a[rel=tag]').
	live('mousedown', function( e ){

            return true;


	}).
	live('click', function( e ){
		if ( !logged_in ) {
			var	target	= original_target(e),
				tag	= $(target).text();
			addfhfilter(tag);
		}
		e.preventDefault();
		return false;
	});

$TAG_MENU.menu({
	cssNamespace: 'slash',
	liveTriggers: true,
	clickDuration: 300,

	start: function( e, ui ){
		var	$tag	= $(ui.trigger),
			tag	= get_tag_name($tag),
			context	= firehose_settings && firehose_settings.viewtitle;

		// Insert the tagname into the menu items where needed.
		$TAG_MENU.find('span.var-tag').text(tag);
		$TAG_MENU.find('a.nix').attr('title','not ' + tag);


			// non-admins may only delete their own tags
		$TAG_MENU.find('a:[data-op="-"]').toggle($tag.is('.my'));


		// *tagname* in *viewtitle*
		$TAG_MENU.find('a:[data-op="="]').toggle(!!context);
		context && $TAG_MENU.find('span.var-view').text(context);

		open_menu($tag, $TAG_MENU);
	},

	select: function( e, ui ){
		var	$tag	= $(ui.trigger),
			tag	= get_tag_name($tag),
			op	= $(ui.select).attr('data-op'),
			fhitem,
			command;

		// Global for positioning other things.
		$related_trigger = $tag;

		switch ( op ) {
			case '=':
				addfhfilter(tag);
				break;

			default:
				fhitem = $tag.closest('.fhitem')[0];
				command = (op + tag).replace(NOTNOT, '');
				try { Tags.submit(fhitem, command); } catch ( err ) {  }
				break;
		}
	},

	stop: function( e, ui ){ close_menu(ui.trigger, $TAG_MENU); }
});




/* T2 feedback context-menu */



/* T2 datatype context-menu (admin-only) */






});
</script>




<div class="container">
	<div class="main-wrap  has-rail-right">
		<div class="main-content">
			<div id="firehose" class="nothumbs ">
				<!-- WIT -->
				<a name="articles"></a>







				<div id="firehoselist" class="fhroot row ">
					<div id="announcement">
 CYBER MONDAY DEAL: Encrypt all of your data and surf the web safely with a lifetime of <strong><a href="https://deals.slashdot.org/sales/vpnsecure-lifetime-3?utm_source=slashdot&utm_medium=announcement-bar&utm_campaign=vpnsecure-lifetime-3">VPNSecure for $24</a></strong> with coupon code "CYBER40"
  <a href="" class="btn-close" title="don't show me this again" onclick="closeAnnouncement(); return false;">&times;</a>
</div>


<script type="text/javascript">

if (!$.cookie('hide_sitenotice_36')) {
	$('#announcement').fadeIn(300);
}

function closeAnnouncement() {
	$('#announcement').fadeOut(300);
	$.cookie('hide_sitenotice_36', 'true', { path: '/', domain: 'slashdot.org', expires: 28 });
}
</script>
					<article id="firehose-95545727" data-fhid="95545727" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95545727</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95545727">
			<a href="//slashdot.org/index2.pl?fhfilter=chrome" onclick="return addfhfilter('chrome');">

				<img src="//a.fsdn.com/sd/topics/chrome_64.png" width="64" height="64" alt="Chrome" title="Chrome">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95545727" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//hardware.slashdot.org/story/17/11/28/023204/microsoft-office-now-available-on-all-chromebooks">Microsoft Office Now Available On All Chromebooks</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://www.theverge.com/2017/11/27/16703952/microsoft-office-now-available-on-all-chromebooks"  title="External link - https://www.theverge.com/2017/11/27/16703952/microsoft-office-now-available-on-all-chromebooks" target="_blank"> (theverge.com) </a></span></span>



		<!--<span class="comments commentcnt-95545727" >4</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//hardware.slashdot.org/story/17/11/28/023204/microsoft-office-now-available-on-all-chromebooks#comments" title="">4</a></span>

	</h2>
	<div class="details" id="details-95545727">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95545727" datetime="on Tuesday November 28, 2017 @05:00AM">on Tuesday November 28, 2017 @05:00AM</time>


			 from the <span class="dept-text">come-and-get-it</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95545727">




		<div id="text-95545727" class="p">


				Microsoft has reportedly finished testing out its Office apps on Chromebooks as a number of Chromebooks <a href="https://www.theverge.com/2017/11/27/16703952/microsoft-office-now-available-on-all-chromebooks">are now seeing the Office apps in the Google Play Store</a>. Samsung's Chromebook Pro, Acer's Chromebook 15, and Acer's C771 have the Office apps available for download. The Verge reports: <i> The apps are Android versions of Office which include the same features you'd find on an Android tablet running Office. Devices like Asus' Chromebook Flip (with a 10.1-inch display) will get free access to Office on Chrome OS, but larger devices will need a subscription. Microsoft has a rule across Windows, iOS, and Android hardware that means devices larger than 10.1 inches need an Office 365 subscription to unlock the ability to create, edit, or print documents. </i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://hardware.slashdot.org/story/17/11/28/023204/microsoft-office-now-available-on-all-chromebooks"
				  data-janrain-title="Microsoft Office Now Available On All Chromebooks"
				  data-janrain-message="Microsoft Office Now Available On All Chromebooks @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95545727" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/android" target="_blank">android</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/chrome" target="_blank">chrome</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/google" target="_blank">google</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95541709" data-fhid="95541709" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95541709</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95541709">
			<a href="//slashdot.org/index2.pl?fhfilter=books" onclick="return addfhfilter('books');">

				<img src="//a.fsdn.com/sd/topics/books_64.png" width="64" height="64" alt="Books" title="Books">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95541709" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//entertainment.slashdot.org/story/17/11/27/2246249/tom-baker-returns-to-finish-shelved-doctor-who-episodes-penned-by-douglas-adams">Tom Baker Returns To Finish Shelved Doctor Who Episodes Penned By Douglas Adams</a> <span class=" no extlnk"><a class="story-sourcelnk" href="http://www.theregister.co.uk/2017/11/27/tom_baker_completes_cancelled_doctor_who_serial_shada/"  title="External link - http://www.theregister.co.uk/2017/11/27/tom_baker_completes_cancelled_doctor_who_serial_shada/" target="_blank"> (theregister.co.uk) </a></span></span>



		<!--<span class="comments commentcnt-95541709" >15</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//entertainment.slashdot.org/story/17/11/27/2246249/tom-baker-returns-to-finish-shelved-doctor-who-episodes-penned-by-douglas-adams#comments" title="">15</a></span>

	</h2>
	<div class="details" id="details-95541709">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95541709" datetime="on Tuesday November 28, 2017 @02:00AM">on Tuesday November 28, 2017 @02:00AM</time>


			 from the <span class="dept-text">blast-from-the-past</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95541709">




		<div id="text-95541709" class="p">


				<a href="/~Zorro">Zorro</a> shares a report from The Register: <i> The fourth and finest Doctor, Tom Baker, has <a href="http://www.theregister.co.uk/2017/11/27/tom_baker_completes_cancelled_doctor_who_serial_shada/">reprised the role to finish a Who serial</a> scuppered in 1979 by strike action at the BBC. Shada, penned by Hitchhiker's Guide author Douglas Adams, was supposed to close Doctor Who's 17th season. Location filming in Cambridge and a studio session were completed but the strike nixed further work and the project was later shelved entirely for fear it might affect the Beeb's Christmas-time productions. The remaining parts have been filled in with animation and the voice of 83-year-old Baker, although he also filmed a scene. BBC Worldwide has now released the episodes, which interweave the 1979 footage with the new material to complete the story. </i> "I loved doing Doctor Who, it was life to me," Baker <a href="http://www.bbc.co.uk/news/uk-england-cambridgeshire-42080978">told the BBC</a> of his tenure as the much-loved Time Lord. "I used to dread the end of rehearsal because then real life would impinge on me. Doctor Who... when I was in full flight, then I was happy."<br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://entertainment.slashdot.org/story/17/11/27/2246249/tom-baker-returns-to-finish-shelved-doctor-who-episodes-penned-by-douglas-adams"
				  data-janrain-title="Tom Baker Returns To Finish Shelved Doctor Who Episodes Penned By Douglas Adams"
				  data-janrain-message="Tom Baker Returns To Finish Shelved Doctor Who Episodes Penned By Douglas Adams @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95541709" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/books" target="_blank">books</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/scifi" target="_blank">scifi</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/tv" target="_blank">tv</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95541851" data-fhid="95541851" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95541851</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95541851">
			<a href="//slashdot.org/index2.pl?fhfilter=robot" onclick="return addfhfilter('robot');">

				<img src="//a.fsdn.com/sd/topics/robot_64.png" width="64" height="64" alt="Robotics" title="Robotics">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95541851" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//hardware.slashdot.org/story/17/11/27/2256228/scientists-have-built-robot-muscles-that-can-lift-1000-times-their-own-weight">Scientists Have Built Robot Muscles That Can Lift 1,000 Times Their Own Weight</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://qz.com/1139028/mit-and-harvard-wyss-scientists-have-built-robot-muscles-that-can-lift-1000-times-their-own-weight/"  title="External link - https://qz.com/1139028/mit-and-harvard-wyss-scientists-have-built-robot-muscles-that-can-lift-1000-times-their-own-weight/" target="_blank"> (qz.com) </a></span></span>



		<!--<span class="comments commentcnt-95541851" >51</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//hardware.slashdot.org/story/17/11/27/2256228/scientists-have-built-robot-muscles-that-can-lift-1000-times-their-own-weight#comments" title="">51</a></span>

	</h2>
	<div class="details" id="details-95541851">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95541851" datetime="on Monday November 27, 2017 @10:30PM">on Monday November 27, 2017 @10:30PM</time>


			 from the <span class="dept-text">origami-inspired</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95541851">




		<div id="text-95541851" class="p">


				An anonymous reader quotes a report from Quartz: <i>Researchers at Harvard's Wyss Institute and MIT's Computer Science and Artificial Intelligence Laboratory (CSAIL) announced today (Nov. 27) that they've <a href="https://qz.com/1139028/mit-and-harvard-wyss-scientists-have-built-robot-muscles-that-can-lift-1000-times-their-own-weight/">created robotic "muscles" that can lift up to 1,000 times their own weight</a>. The simple objects are constructed out of metal or plastic "skeletons" that are covered in either a liquid or air, and then sealed in plastic or fabric "skins." The muscle pulls taught when a vacuum is created inside the skin, and goes slack when the vacuum is released. By folding the skeletons in different ways, the vacuum can pull the muscle in different directions. "Vacuum-based muscles have a lower risk of rupture, failure, and damage, and they don't expand when they're operating, so you can integrate them into closer-fitting robots on the human body," Daniel Vogt, a research engineer at the Wyss Institute, <a href="https://wyss.harvard.edu/artificial-muscles-give-soft-robots-superpowers/">said in a release</a>.
<br> <br>
These new structures are also surprisingly cheap. As they don't require anything other than water or air to move them, the researchers told Harvard that a single muscle can be built in about 10 minutes, for less than $1. (Obviously, there'd still be a cost for the vacuum or whatever is being used to change the pressure of the muscles.)</i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://hardware.slashdot.org/story/17/11/27/2256228/scientists-have-built-robot-muscles-that-can-lift-1000-times-their-own-weight"
				  data-janrain-title="Scientists Have Built Robot Muscles That Can Lift 1,000 Times Their Own Weight"
				  data-janrain-message="Scientists Have Built Robot Muscles That Can Lift 1,000 Times Their Own Weight @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95541851" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/mit" target="_blank">mit</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/robot" target="_blank">robot</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/science" target="_blank">science</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95542003" data-fhid="95542003" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95542003</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95542003">
			<a href="//slashdot.org/index2.pl?fhfilter=android" onclick="return addfhfilter('android');">

				<img src="//a.fsdn.com/sd/topics/android_64.png" width="64" height="64" alt="Android" title="Android">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95542003" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//mobile.slashdot.org/story/17/11/27/232244/the-pixel-2s-dormant-visual-core-chip-gets-activated-in-latest-android-developer-preview">The Pixel 2's Dormant 'Visual Core' Chip Gets Activated In Latest Android Developer Preview</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://techcrunch.com/2017/11/27/the-pixel-2s-dormant-visual-core-chip-gets-activated-in-the-latest-android-developer-preview/"  title="External link - https://techcrunch.com/2017/11/27/the-pixel-2s-dormant-visual-core-chip-gets-activated-in-the-latest-android-developer-preview/" target="_blank"> (techcrunch.com) </a></span></span>



		<!--<span class="comments commentcnt-95542003" >19</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//mobile.slashdot.org/story/17/11/27/232244/the-pixel-2s-dormant-visual-core-chip-gets-activated-in-latest-android-developer-preview#comments" title="">19</a></span>

	</h2>
	<div class="details" id="details-95542003">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95542003" datetime="on Monday November 27, 2017 @09:05PM">on Monday November 27, 2017 @09:05PM</time>


			 from the <span class="dept-text">latest-and-greatest</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95542003">




		<div id="text-95542003" class="p">


				The Google Pixel 2 and Pixel 2 XL both feature a <a href="https://tech.slashdot.org/story/17/10/23/1950248/google-worked-with-intel-on-a-custom-ai-chip-for-its-pixel-phones">custom Intel "Visual Core" co-processor</a>, which is meant to improve speed and battery life when shooting photos with Google's HDR+ technology. The chip has been hanging out in the phone not really doing much of anything -- until now. TechCrunch reports of a <a href="https://android-developers.googleblog.com/2017/11/final-preview-of-android-81-now.html">new developer preview of Android 8.1</a> due out today that puts the chip to use. "The component is <a href="https://techcrunch.com/2017/11/27/the-pixel-2s-dormant-visual-core-chip-gets-activated-in-the-latest-android-developer-preview/">expected to further improve the handsets' cameras</a>, which were already scoring good marks, production issues aside." From the report: <i> According to the company, Pixel Visual Core has eight image processing unit (IPU) cores and 512 arithmetic logic units. Using machine learning, the company says it's able to speed things up by 5x, with one tenth of the energy. Access to the chip, combined with the Android Camera API means third-party photo apps will be able to take advantage of the system's speedy HDR+. Sounds swell, right? Of course, this is still just an early preview, only available to people who sign up for Google's Beta program. That means, among other things, dealing with potential bugs of an early build. Google wouldn't give us any more specific information with regards to when the feature will be unlocked for the public, but it's expected to arrive along with the 8.1 public beta in December. </i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://mobile.slashdot.org/story/17/11/27/232244/the-pixel-2s-dormant-visual-core-chip-gets-activated-in-latest-android-developer-preview"
				  data-janrain-title="The Pixel 2's Dormant 'Visual Core' Chip Gets Activated In Latest Android Developer Preview"
				  data-janrain-message="The Pixel 2's Dormant 'Visual Core' Chip Gets Activated In Latest Android Developer Preview @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95542003" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/android" target="_blank">android</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/google" target="_blank">google</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/os" target="_blank">os</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95539939" data-fhid="95539939" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95539939</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95539939">
			<a href="//slashdot.org/index2.pl?fhfilter=ai" onclick="return addfhfilter('ai');">

				<img src="//a.fsdn.com/sd/topics/ai_64.png" width="64" height="64" alt="AI" title="AI">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95539939" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//tech.slashdot.org/story/17/11/27/2110247/facebook-rolls-out-ai-to-detect-suicidal-posts-before-theyre-reported">Facebook Rolls Out AI To Detect Suicidal Posts Before They're Reported</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://techcrunch.com/2017/11/27/facebook-ai-suicide-prevention/"  title="External link - https://techcrunch.com/2017/11/27/facebook-ai-suicide-prevention/" target="_blank"> (techcrunch.com) </a></span></span>



		<!--<span class="comments commentcnt-95539939" >104</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//tech.slashdot.org/story/17/11/27/2110247/facebook-rolls-out-ai-to-detect-suicidal-posts-before-theyre-reported#comments" title="">104</a></span>

	</h2>
	<div class="details" id="details-95539939">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95539939" datetime="on Monday November 27, 2017 @08:25PM">on Monday November 27, 2017 @08:25PM</time>


			 from the <span class="dept-text">proactive-detection</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95539939">




		<div id="text-95539939" class="p">


				Facebook is rolling out "proactive detection" artificial intelligence technology that <a href="https://techcrunch.com/2017/11/27/facebook-ai-suicide-prevention/">will scan all posts on the site for patterns of suicidal thoughts</a>, and when necessary send mental health resources to the user at risk or their friends, or contact local first-responders. The goal is to use AI to decrease how long it takes to send help to those in need. TechCrunch reports: <i> Facebook <a href="https://newsroom.fb.com/news/2017/03/building-a-safer-community-with-new-suicide-prevention-tools/">previously</a> tested using AI to detect troubling posts and more prominently surface suicide reporting options to friends in the U.S. Now Facebook is will scour all types of content <a href="https://newsroom.fb.com/news/2017/11/getting-our-community-help-in-real-time/">around the world</a> with this AI, except in the European Union, where <a href="http://privacylawblog.fieldfisher.com/2017/let-s-sort-out-this-profiling-and-consent-debate-once-and-for-all/">General Data Protection Regulation</a> privacy laws on profiling users based on sensitive information complicate the use of this tech. Facebook also will use AI to prioritize particularly risky or urgent user reports so they're more quickly addressed by moderators, and tools to instantly surface local language resources and first-responder contact info. It's also dedicating more moderators to suicide prevention, training them to deal with the cases 24/7, and now has 80 local partners like Save.org, National Suicide Prevention Lifeline and Forefront from which to provide resources to at-risk users and their networks. </i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://tech.slashdot.org/story/17/11/27/2110247/facebook-rolls-out-ai-to-detect-suicidal-posts-before-theyre-reported"
				  data-janrain-title="Facebook Rolls Out AI To Detect Suicidal Posts Before They're Reported"
				  data-janrain-message="Facebook Rolls Out AI To Detect Suicidal Posts Before They're Reported @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95539939" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/facebook" target="_blank">facebook</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/health" target="_blank">health</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/internet" target="_blank">internet</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95539749" data-fhid="95539749" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95539749</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95539749">
			<a href="//slashdot.org/index2.pl?fhfilter=cellphones" onclick="return addfhfilter('cellphones');">

				<img src="//a.fsdn.com/sd/topics/cellphones_64.png" width="64" height="64" alt="Cellphones" title="Cellphones">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95539749" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//games.slashdot.org/story/17/11/27/214256/pokemon-go-led-to-increase-in-traffic-deaths-and-accidents-says-study">Pokemon Go Led To Increase In Traffic Deaths and Accidents, Says Study</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://arstechnica.com/gaming/2017/11/study-pokemon-go-led-to-increase-in-traffic-deaths-accidents/"  title="External link - https://arstechnica.com/gaming/2017/11/study-pokemon-go-led-to-increase-in-traffic-deaths-accidents/" target="_blank"> (arstechnica.com) </a></span></span>



		<!--<span class="comments commentcnt-95539749" >46</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//games.slashdot.org/story/17/11/27/214256/pokemon-go-led-to-increase-in-traffic-deaths-and-accidents-says-study#comments" title="">46</a></span>

	</h2>
	<div class="details" id="details-95539749">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95539749" datetime="on Monday November 27, 2017 @07:45PM">on Monday November 27, 2017 @07:45PM</time>


			 from the <span class="dept-text">fun-while-it-lasted</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95539749">




		<div id="text-95539749" class="p">


				A <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3073723">new study</a> from Purdue University uses detailed local traffic accident reports to suggest that Pokemon Go <a href="https://arstechnica.com/gaming/2017/11/study-pokemon-go-led-to-increase-in-traffic-deaths-accidents/">caused a marked increase in vehicle damages, injuries, and even deaths</a> due to people playing the game while driving. Ars Technica reports: <i> In the provocatively titled "Death by Pokemon Go" (which has been shared online but has yet to be peer-reviewed), Purdue professors Mara Faccio and John J. McConnell studied nearly 12,000 accident reports in Tippecanoe County, Indiana, in the months before and after Pokemon Go's July 6, 2016 launch. The authors then cross-referenced those reports with the locations of Pokestops in the county (where players visit frequently to obtain necessary in-game items) to determine whether the introduction of a Pokestop correlated with an increase in accident frequency, relative to intersections that didn't have them. While the incidence of traffic accidents increased across the county after Pokemon Go's introduction, that increase was a statistically significant 26.5 percent greater at intersections within 100 meters of a Pokestop, compared to those farther away. All told, across the county, the authors estimate 134 extra accidents occurred near Pokestops in the 148-day period immediately after the game came out, compared to the baseline where those Pokestops didn't exist. That adds up to nearly $500,000 in vehicle damage, 31 additional injuries, and two additional deaths across the county, based on extrapolation from the accident reports. <br> <br> The study uses a regression model to account for potential confounding variables like school breaks and inclement weather, which could cause variation separate from Pokemon Go. The model also compares Pokestops to Pokegyms (where it was nearly impossible to play while driving) to account for the possibility that generally increased traffic to Pokemon Go locations was leading to more accidents, even among drivers who stopped and parked before playing. In all cases, though, being able to compare to intersections without a Pokestop and to the same dates the year before, helped provide natural control variables for the study. </i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://games.slashdot.org/story/17/11/27/214256/pokemon-go-led-to-increase-in-traffic-deaths-and-accidents-says-study"
				  data-janrain-title="Pokemon Go Led To Increase In Traffic Deaths and Accidents, Says Study"
				  data-janrain-message="Pokemon Go Led To Increase In Traffic Deaths and Accidents, Says Study @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95539749" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/death" target="_blank">death</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/games" target="_blank">games</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/mobile" target="_blank">mobile</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95540289" data-fhid="95540289" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95540289</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95540289">
			<a href="//slashdot.org/index2.pl?fhfilter=bug" onclick="return addfhfilter('bug');">

				<img src="//a.fsdn.com/sd/topics/bug_64.png" width="64" height="64" alt="Bug" title="Bug">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95540289" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//it.slashdot.org/story/17/11/27/2124201/iphone-users-complain-about-the-word-it-autocorrecting-to-it-on-ios-11-and-later">iPhone Users Complain About the Word 'It' Autocorrecting To 'I.T' On iOS 11 and Later</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://www.macrumors.com/2017/11/27/ios-11-autocorrect-issue-it-to-i-t/"  title="External link - https://www.macrumors.com/2017/11/27/ios-11-autocorrect-issue-it-to-i-t/" target="_blank"> (macrumors.com) </a></span></span>



		<!--<span class="comments commentcnt-95540289" >73</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//it.slashdot.org/story/17/11/27/2124201/iphone-users-complain-about-the-word-it-autocorrecting-to-it-on-ios-11-and-later#comments" title="">73</a></span>

	</h2>
	<div class="details" id="details-95540289">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95540289" datetime="on Monday November 27, 2017 @07:05PM">on Monday November 27, 2017 @07:05PM</time>


			 from the <span class="dept-text">buggy-software</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95540289">




		<div id="text-95540289" class="p">


				An anonymous reader quotes a report from MacRumors: <i>At least a few hundred iPhone users and counting have <a href="https://www.macrumors.com/2017/11/27/ios-11-autocorrect-issue-it-to-i-t/">complained about the word "it" autocorrecting to "I.T" on iOS 11 and later</a>. When affected users type the word "it" into a text field, the keyboard first shows "I.T" as a QuickType suggestion. After tapping the space key, the word "it" automatically changes to "I.T" without actually tapping the predictive suggestion. A growing number of iPhone users have voiced their frustrations about the issue on the <a href="https://forums.macrumors.com/threads/new-weird-autocorrect-bug.2090295/">MacRumors discussion forums</a>, <a href="https://mobile.twitter.com/search?f=tweets&amp;vertical=default&amp;mr&amp;q=it%20i.t.%20apple&amp;src=typd">Twitter</a>, and other discussion platforms on the web <a href="https://forums.macrumors.com/threads/reset-keyboard-issue.2070774/">since shortly after iOS 11 was released</a> in late September. Many users claim the apparent autocorrect bug persists even after rebooting the device and performing other basic troubleshooting.  A temporary workaround is to tap Settings: General: Keyboard: Text Replacement and enter "it" as both the phrase and shortcut, but some users insist this solution does not solve the problem. A less ideal workaround is to toggle off auto-correction and/or predictive suggestions completely under Settings: General: Keyboard.</i> MacRumors reader Tim <a href="https://www.youtube.com/watch?v=pNlHDViN3z8">shared a video</a> that highlights the issue.<br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://it.slashdot.org/story/17/11/27/2124201/iphone-users-complain-about-the-word-it-autocorrecting-to-it-on-ios-11-and-later"
				  data-janrain-title="iPhone Users Complain About the Word 'It' Autocorrecting To 'I.T' On iOS 11 and Later"
				  data-janrain-message="iPhone Users Complain About the Word 'It' Autocorrecting To 'I.T' On iOS 11 and Later @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95540289" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/apple" target="_blank">apple</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/bug" target="_blank">bug</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/iphone" target="_blank">iphone</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95540419" data-fhid="95540419" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95540419</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95540419">
			<a href="//slashdot.org/index2.pl?fhfilter=cellphones" onclick="return addfhfilter('cellphones');">

				<img src="//a.fsdn.com/sd/topics/cellphones_64.png" width="64" height="64" alt="Cellphones" title="Cellphones">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95540419" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//it.slashdot.org/story/17/11/27/2133242/white-house-weighs-personal-mobile-phone-ban-for-staff">White House Weighs Personal Mobile Phone Ban For Staff</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://www.bloomberg.com/news/articles/2017-11-27/white-house-is-said-to-weigh-personal-mobile-phone-ban-for-staff"  title="External link - https://www.bloomberg.com/news/articles/2017-11-27/white-house-is-said-to-weigh-personal-mobile-phone-ban-for-staff" target="_blank"> (bloomberg.com) </a></span></span>



		<!--<span class="comments commentcnt-95540419" >83</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//it.slashdot.org/story/17/11/27/2133242/white-house-weighs-personal-mobile-phone-ban-for-staff#comments" title="">83</a></span>

	</h2>
	<div class="details" id="details-95540419">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95540419" datetime="on Monday November 27, 2017 @06:20PM">on Monday November 27, 2017 @06:20PM</time>


			 from the <span class="dept-text">unauthorized-news-leaks</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95540419">




		<div id="text-95540419" class="p">


				The White House is <a href="https://www.bloomberg.com/news/articles/2017-11-27/white-house-is-said-to-weigh-personal-mobile-phone-ban-for-staff">considering banning its employees from using personal mobile phones while at work</a>. While President Trump has been vocal about press leaks since taking office, one official said the potential change is driven by cybersecurity concerns. Bloomberg reports: <i> One official said that there are too many devices connected to the campus wireless network and that personal phones aren't as secure as those issued by the federal government. White House Chief of Staff John Kelly -- whose personal phone was <a href="https://yro.slashdot.org/story/17/10/06/2027202/white-house-chief-of-staffs-phone-was-reportedly-hacked-months-ago">found to be compromised by hackers</a> earlier this year -- is leading the push for a ban, another official said. The White House already takes precautions with personal wireless devices, including by requiring officials to leave phones in cubbies outside of meeting rooms where sensitive or classified information is discussed. Top officials haven't yet decided whether or when to impose the ban, and if it would apply to all staff in the executive office of the president. While some lower-level officials support a ban, others worry it could result in a series of disruptive unintended consequences. </i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://it.slashdot.org/story/17/11/27/2133242/white-house-weighs-personal-mobile-phone-ban-for-staff"
				  data-janrain-title="White House Weighs Personal Mobile Phone Ban For Staff"
				  data-janrain-message="White House Weighs Personal Mobile Phone Ban For Staff @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95540419" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/mobile" target="_blank">mobile</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/privacy" target="_blank">privacy</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/security" target="_blank">security</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95539449" data-fhid="95539449" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95539449</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95539449">
			<a href="//slashdot.org/index2.pl?fhfilter=advertising" onclick="return addfhfilter('advertising');">

				<img src="//a.fsdn.com/sd/topics/advertising_64.png" width="64" height="64" alt="Advertising" title="Advertising">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95539449" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//news.slashdot.org/story/17/11/27/2050215/plexs-dvr-can-now-automatically-remove-commercials-for-you">Plex's DVR Can Now Automatically Remove Commercials For You</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://www.digitaltrends.com/home-theater/plex-dvr-removes-commercials/"  title="External link - https://www.digitaltrends.com/home-theater/plex-dvr-removes-commercials/" target="_blank"> (digitaltrends.com) </a></span></span>



		<!--<span class="comments commentcnt-95539449" >56</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//news.slashdot.org/story/17/11/27/2050215/plexs-dvr-can-now-automatically-remove-commercials-for-you#comments" title="">56</a></span>

	</h2>
	<div class="details" id="details-95539449">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95539449" datetime="on Monday November 27, 2017 @05:40PM">on Monday November 27, 2017 @05:40PM</time>


			 from the <span class="dept-text">magic-wand</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95539449">




		<div id="text-95539449" class="p">


				Plex has updated its DVR, <a href="https://www.digitaltrends.com/home-theater/plex-dvr-removes-commercials/">adding a new feature to automatically remove commercials</a>. According to Digital Trends, "The feature was added in an update the Plex team pushed out over the weekend. You'll need to manually enable the feature by heading into your Plex DVR settings and finding the option, labeled 'Remove Commercials.'" From the report: <i> You may not want to turn the feature on immediately without looking into reports from other users. The description in the settings warns that while the feature will attempt to automatically locate and remove commercials, this could potentially take a long time and cause high CPU usage. If you're running your Plex server on a powerful computer, this may not be an issue, but if you're running it on an old laptop, you might want to hold off. This new feature also changes your DVR recordings permanently, removing commercials from the files themselves. This shouldn't be a problem as long as the feature works as intended, but if it detects wrong portions of the file as commercials, you could end up missing out on part of your favorite shows. </i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://news.slashdot.org/story/17/11/27/2050215/plexs-dvr-can-now-automatically-remove-commercials-for-you"
				  data-janrain-title="Plex's DVR Can Now Automatically Remove Commercials For You"
				  data-janrain-message="Plex's DVR Can Now Automatically Remove Commercials For You @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95539449" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/dvr" target="_blank">dvr</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/media" target="_blank">media</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/movies" target="_blank">movies</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95538649" data-fhid="95538649" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95538649</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95538649">
			<a href="//slashdot.org/index2.pl?fhfilter=internet" onclick="return addfhfilter('internet');">

				<img src="//a.fsdn.com/sd/topics/internet_64.png" width="64" height="64" alt="The Internet" title="The Internet">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95538649" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//tech.slashdot.org/story/17/11/27/2030223/comcast-hints-at-plan-for-paid-fast-lanes-after-net-neutrality-repeal">Comcast Hints At Plan For Paid Fast Lanes After Net Neutrality Repeal</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://arstechnica.com/tech-policy/2017/11/comcast-quietly-drops-promise-not-to-charge-tolls-for-internet-fast-lanes/"  title="External link - https://arstechnica.com/tech-policy/2017/11/comcast-quietly-drops-promise-not-to-charge-tolls-for-internet-fast-lanes/" target="_blank"> (arstechnica.com) </a></span></span>



		<!--<span class="comments commentcnt-95538649" >212</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//tech.slashdot.org/story/17/11/27/2030223/comcast-hints-at-plan-for-paid-fast-lanes-after-net-neutrality-repeal#comments" title="">212</a></span>

	</h2>
	<div class="details" id="details-95538649">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  <a href="https://twitter.com/BeauHD" rel="nofollow">BeauHD</a>






		<time id="fhtime-95538649" datetime="on Monday November 27, 2017 @05:00PM">on Monday November 27, 2017 @05:00PM</time>


			 from the <span class="dept-text">carefully-worded</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95538649">




		<div id="text-95538649" class="p">


				An anonymous reader quotes a report from Ars Technica: <i>For years, Comcast has been promising that it won't violate the principles of net neutrality, regardless of whether the government imposes any net neutrality rules. That meant that Comcast wouldn't block or throttle lawful Internet traffic and that it wouldn't create fast lanes in order to collect tolls from Web companies that want priority access over the Comcast network. This was one of the ways in which Comcast argued that the Federal Communications Commission should not reclassify broadband providers as common carriers, a designation that forces ISPs to treat customers fairly in other ways. The Title II common carrier classification that makes net neutrality rules enforceable isn't necessary because ISPs won't violate net neutrality principles anyway, Comcast and other ISPs have claimed. <br> <br>But with Republican Ajit Pai now in charge at the Federal Communications Commission, Comcast's stance has changed. While the company still says it won't block or throttle Internet content, it has <a href="https://arstechnica.com/tech-policy/2017/11/comcast-quietly-drops-promise-not-to-charge-tolls-for-internet-fast-lanes/">dropped its promise about not instituting paid prioritization</a>. Instead, Comcast now vaguely <a href="https://twitter.com/comcast?ref_src=twsrc%5Etfw&amp;ref_url=https%3A%2F%2Farstechnica.com%2Ftech-policy%2F2017%2F11%2Fcomcast-quietly-drops-promise-not-to-charge-tolls-for-internet-fast-lanes%2F">says</a> that it won't "discriminate against lawful content" or impose "anti-competitive paid prioritization." The change in wording suggests that Comcast may offer paid fast lanes to websites or other online services, such as video streaming providers, after Pai's FCC eliminates the net neutrality rules next month.</i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://tech.slashdot.org/story/17/11/27/2030223/comcast-hints-at-plan-for-paid-fast-lanes-after-net-neutrality-repeal"
				  data-janrain-title="Comcast Hints At Plan For Paid Fast Lanes After Net Neutrality Repeal"
				  data-janrain-message="Comcast Hints At Plan For Paid Fast Lanes After Net Neutrality Repeal @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95538649" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/business" target="_blank">business</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/comcast" target="_blank">comcast</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/fcc" target="_blank">fcc</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95538517" data-fhid="95538517" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95538517</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95538517">
			<a href="//slashdot.org/index2.pl?fhfilter=education" onclick="return addfhfilter('education');">

				<img src="//a.fsdn.com/sd/topics/education_64.png" width="64" height="64" alt="Education" title="Education">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95538517" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//news.slashdot.org/story/17/11/27/2019250/computer-science-gcse-in-disarray-after-tasks-leaked-online">Computer Science GCSE in Disarray After Tasks Leaked Online</a> <span class=" no extlnk"><a class="story-sourcelnk" href="http://www.bbc.com/news/education-42138037"  title="External link - http://www.bbc.com/news/education-42138037" target="_blank"> (bbc.com) </a></span></span>



		<!--<span class="comments commentcnt-95538517" >44</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//news.slashdot.org/story/17/11/27/2019250/computer-science-gcse-in-disarray-after-tasks-leaked-online#comments" title="">44</a></span>

	</h2>
	<div class="details" id="details-95538517">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  msmash






		<time id="fhtime-95538517" datetime="on Monday November 27, 2017 @04:20PM">on Monday November 27, 2017 @04:20PM</time>


			 from the <span class="dept-text">security-woes</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95538517">




		<div id="text-95538517" class="p">


				An anonymous reader shares a report:<i> The new computer science GCSE has been thrown into disarray after programming tasks worth <a href="http://www.bbc.com/news/education-42138037">a fifth of the total marks were leaked repeatedly online</a>. Exams regulator Ofqual plans to pull this chunk of the qualification from the overall marks as it has been seen by thousands of people. Ofqual said the non-exam assessment may have been leaked by teachers as well as students who had completed the task. The breach affects two year groups. The first will sit the exam in summer 2018. Last year 70,000 students were entered for computer science GCSE. A quick internet search reveals numerous posts about the the non-exam assessment, with questions and potential answers.</i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://news.slashdot.org/story/17/11/27/2019250/computer-science-gcse-in-disarray-after-tasks-leaked-online"
				  data-janrain-title="Computer Science GCSE in Disarray After Tasks Leaked Online"
				  data-janrain-message="Computer Science GCSE in Disarray After Tasks Leaked Online @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95538517" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/security" target="_blank">security</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/uk" target="_blank">uk</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/education" target="_blank">education</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95538317" data-fhid="95538317" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95538317</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95538317">
			<a href="//slashdot.org/index2.pl?fhfilter=business" onclick="return addfhfilter('business');">

				<img src="//a.fsdn.com/sd/topics/business_64.png" width="64" height="64" alt="Businesses" title="Businesses">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95538317" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//yro.slashdot.org/story/17/11/27/207251/reddit-twitter-and-200-others-say-ending-net-neutrality-could-ruin-cyber-monday">Reddit, Twitter, and 200 Others Say Ending Net Neutrality Could Ruin Cyber Monday</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://www.theverge.com/2017/11/27/16705170/net-neutrality-cyber-monday-fcc-letter"  title="External link - https://www.theverge.com/2017/11/27/16705170/net-neutrality-cyber-monday-fcc-letter" target="_blank"> (theverge.com) </a></span></span>



		<!--<span class="comments commentcnt-95538317" >83</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//yro.slashdot.org/story/17/11/27/207251/reddit-twitter-and-200-others-say-ending-net-neutrality-could-ruin-cyber-monday#comments" title="">83</a></span>

	</h2>
	<div class="details" id="details-95538317">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  msmash






		<time id="fhtime-95538317" datetime="on Monday November 27, 2017 @03:40PM">on Monday November 27, 2017 @03:40PM</time>


			 from the <span class="dept-text">avengers,-unite</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95538317">




		<div id="text-95538317" class="p">


				An anonymous reader shares a report:<i> More than 200 businesses and trade organizations have signed a letter to the FCC asking that the <a href="https://www.theverge.com/2017/11/27/16705170/net-neutrality-cyber-monday-fcc-letter">agency reconsider its plan to end net neutrality</a>. The letter is signed by an array of big and recognizable tech and web companies: that includes Airbnb, Automattic (which owns WordPress), Etsy, Foursquare, GitHub, Pinterest, Reddit, Shutterstock, Sonos, Square, Squarespace, Tumblr (certainly to the displeasure of its owner, Verizon), Twitter, and Vimeo, among quite a few others. The <a href="https://docs.google.com/document/d/14NM8kSCe0v8D1AzhYan4nuToTpXn_N7CRs-fqa68IPg/edit">letter</a> is being released on Cyber Monday and speaks directly to the internet's constantly growing role in the US economy. "The internet is increasingly where commerce happens," the letter says. It cites figures saying that $3.5 billion in online sales happed last year on Cyber Monday and $3 billion on Black Friday. Throughout all of last year, online purchases accounted for $400 billion in sales.</i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://yro.slashdot.org/story/17/11/27/207251/reddit-twitter-and-200-others-say-ending-net-neutrality-could-ruin-cyber-monday"
				  data-janrain-title="Reddit, Twitter, and 200 Others Say Ending Net Neutrality Could Ruin Cyber Monday"
				  data-janrain-message="Reddit, Twitter, and 200 Others Say Ending Net Neutrality Could Ruin Cyber Monday @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95538317" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/business" target="_blank">business</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/usa" target="_blank">usa</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/yro" target="_blank">yro</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article onclick="javascript:return false;"  id="firehose-95537889" data-fhid="95537889" data-fhtype="story" class="fhitem fhitem-story briefarticle usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95537889</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95537889">
			<a href="//slashdot.org/index2.pl?fhfilter=usa" onclick="return addfhfilter('usa');">

				<img src="//a.fsdn.com/sd/topics/usa_64.png" width="64" height="64" alt="United States" title="United States">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95537889" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//politics.slashdot.org/story/17/11/27/1946238/complicit-is-the-word-of-the-year-in-2017-dictionarycom-says">'Complicit' Is The Word Of The Year In 2017, Dictionary.com Says</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://www.npr.org/sections/thetwo-way/2017/11/27/566763885/complicit-is-the-word-of-the-year-in-2017-dictionary-com-says"  title="External link - https://www.npr.org/sections/thetwo-way/2017/11/27/566763885/complicit-is-the-word-of-the-year-in-2017-dictionary-com-says" target="_blank"> (npr.org) </a></span></span>



		<!--<span class="comments commentcnt-95537889" >62</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//politics.slashdot.org/story/17/11/27/1946238/complicit-is-the-word-of-the-year-in-2017-dictionarycom-says#comments" title="">62</a></span>

	</h2>
	<div class="details" id="details-95537889">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'orange')" title="Filter Firehose to entries rated orange or better"></span><span class="icon-beaker pop2 " alt="Popularity" title="Filter Firehose to entries rated orange or better" onclick="firehose_set_options('color', 'orange')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  msmash






		<time id="fhtime-95537889" datetime="on Monday November 27, 2017 @03:00PM">on Monday November 27, 2017 @03:00PM</time>


			 from the <span class="dept-text">word</span> dept.

		</span>
	</div>
</header>

<div class="hide" id="fhbody-95537889">




		<div id="text-95537889" class="p">


				Dictionary.com has selected "complicit" as its word of the year for 2017, citing the term's renewed relevance in U.S. culture and politics -- and noting that <a href="https://www.npr.org/sections/thetwo-way/2017/11/27/566763885/complicit-is-the-word-of-the-year-in-2017-dictionary-com-says">a refusal to be complicit has also been "a grounding force of 2017."</a> From a report:<i> The website defines "complicit" as "choosing to be involved in an illegal or questionable act, especially with others; having complicity." Interest in the word spiked several times this year, Dictionary.com says -- most notably when Ivanka Trump said in April, "I don't know what it means to be complicit."</i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://politics.slashdot.org/story/17/11/27/1946238/complicit-is-the-word-of-the-year-in-2017-dictionarycom-says"
				  data-janrain-title="'Complicit' Is The Word Of The Year In 2017, Dictionary.com Says"
				  data-janrain-message="'Complicit' Is The Word Of The Year In 2017, Dictionary.com Says @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95537889" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/politics" target="_blank">politics</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/usa" target="_blank">usa</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/english" target="_blank">english</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95537319" data-fhid="95537319" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95537319</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95537319">
			<a href="//slashdot.org/index2.pl?fhfilter=business" onclick="return addfhfilter('business');">

				<img src="//a.fsdn.com/sd/topics/business_64.png" width="64" height="64" alt="Businesses" title="Businesses">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95537319" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//tech.slashdot.org/story/17/11/27/1917219/tumblr-is-tumbling">Tumblr Is Tumbling</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://medium.com/@somospostpc/tumblr-is-tumbling-d6deb3bb831e"  title="External link - https://medium.com/@somospostpc/tumblr-is-tumbling-d6deb3bb831e" target="_blank"> (medium.com) </a></span></span>



		<!--<span class="comments commentcnt-95537319" >140</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//tech.slashdot.org/story/17/11/27/1917219/tumblr-is-tumbling#comments" title="">140</a></span>

	</h2>
	<div class="details" id="details-95537319">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  msmash






		<time id="fhtime-95537319" datetime="on Monday November 27, 2017 @02:20PM">on Monday November 27, 2017 @02:20PM</time>


			 from the <span class="dept-text">roadblocks</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95537319">




		<div id="text-95537319" class="p">


				Alex Barredo, a technology writer, shares his observation on Tumblr's popularity over the past few years:<i> Tumblr is the home of some of the most creative online personas, and now it is dying. Or so it seems. Founded on early 2007 by David Karp with a new formula for really simplified blogging, it quickly took off. With each passing quarter, most of their stats were crushing it. It was the new star of the New York tech scene. The East Coast had a good social platform after years of Californian monopoly (MySpace, Bebo, Facebook, Twitter, etc), at last. In May of 2013, Yahoo snatched it for a cool $1.1 billion: $990 million plus liabilities. Less than a year after the deal was closed, Tumblr peaked in activity. By February of 2014, there were more than 106 million new posts each day on the platform. Today that figure has been <a href="https://medium.com/@somospostpc/tumblr-is-tumbling-d6deb3bb831e">slashed by two thirds to around 35 million</a>.</i> David Karp, the founder of Tumblr, said today <a href="https://twitter.com/davidkarp/status/935216243262574595">he was leaving the company</a>. Karp founded Tumblr close to 11 years ago with Marco Arment. He wrote:<i> I beg you to understand that my decision comes after months of reflection on my personal ambitions, and at no cost to my hopefulness for Tumblr's future or the impact I know it can have. The internet is at a crossroads of which this team can play a fundamental role in shaping. You are in the driver seat, and I am so excited to see where you go!</i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://tech.slashdot.org/story/17/11/27/1917219/tumblr-is-tumbling"
				  data-janrain-title="Tumblr Is Tumbling"
				  data-janrain-message="Tumblr Is Tumbling @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95537319" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/business" target="_blank">business</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/social" target="_blank">social</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/yahoo" target="_blank">yahoo</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article><article id="firehose-95536639" data-fhid="95536639" data-fhtype="story" class="fhitem fhitem-story article usermode thumbs grid_24">
		<span class="sd-info-block" style="display: none">
			<span class="sd-key-firehose-id">95536639</span>
			<span class="type">story</span>

		</span>










<header>

		<span class="topic" id="topic-95536639">
			<a href="//slashdot.org/index2.pl?fhfilter=iphone" onclick="return addfhfilter('iphone');">

				<img src="//a.fsdn.com/sd/topics/iphone_64.png" width="64" height="64" alt="Iphone" title="Iphone">

		</a>
		</span>


	<h2 class="story">













		<span id="title-95536639" class="story-title"> <a onclick="return toggle_fh_body_wrap_return(this);"  href="//apple.slashdot.org/story/17/11/27/1840232/two-major-cydia-hosts-shut-down-as-jailbreaking-fades-in-popularity">Two Major Cydia Hosts Shut Down as Jailbreaking Fades in Popularity</a> <span class=" no extlnk"><a class="story-sourcelnk" href="https://www.macrumors.com/2017/11/23/modmyi-macciti-cydia-repos-shut-down/"  title="External link - https://www.macrumors.com/2017/11/23/modmyi-macciti-cydia-repos-shut-down/" target="_blank"> (macrumors.com) </a></span></span>



		<!--<span class="comments commentcnt-95536639" >84</span>-->



		<!-- comment bubble -->

			<span class="comment-bubble"><a href="//apple.slashdot.org/story/17/11/27/1840232/two-major-cydia-hosts-shut-down-as-jailbreaking-fades-in-popularity#comments" title="">84</a></span>

	</h2>
	<div class="details" id="details-95536639">
		<span class="story-details">
		<span class="story-views">
			<span class="sodify" onclick="firehose_set_options('color', 'red')" title="Filter Firehose to entries rated red or better"></span><span class="icon-beaker pop1 " alt="Popularity" title="Filter Firehose to entries rated red or better" onclick="firehose_set_options('color', 'red')"><span></span></span>
		</span>
		</span>
		<span class="story-byline">


			Posted
				by



				  msmash






		<time id="fhtime-95536639" datetime="on Monday November 27, 2017 @01:41PM">on Monday November 27, 2017 @01:41PM</time>


			 from the <span class="dept-text">end-of-an-era</span> dept.

		</span>
	</div>
</header>

<div class="body" id="fhbody-95536639">




		<div id="text-95536639" class="p">


				Joe Rossignol, writing for MacRumors:<i> ModMy last week announced it has archived its default ModMyi repository on Cydia, which is essentially an alternative App Store for downloading apps, themes, tweaks, and other files on jailbroken iPhone, iPad, and iPod touch devices. ZodTTD/MacCiti also shut down this month, meaning that <a href="https://www.macrumors.com/2017/11/23/modmyi-macciti-cydia-repos-shut-down/">two out of three of Cydia's major default repositories are no longer active as of this month</a>. ModMy recommends developers in the jailbreaking community use the BigBoss repository, which is one of the last major Cydia sources that remains functional. The closure of two major Cydia repositories is arguably the result of a declining interest in jailbreaking, which provides root filesystem access and allows users to modify iOS and install unapproved apps on an iPhone, iPad, or iPod touch. When the iPhone and iPod touch were first released in 2007, jailbreaking quickly grew in popularity for both fun and practical reasons. Before the App Store, for example, it allowed users to install apps and games. Jailbreaking was even useful for something as simple as setting a wallpaper, not possible on early iOS versions.</i><br>

		</div>






	</div>
	<aside class="novote">

	</aside>




		<footer class="clearfix meta article-foot">
			<div class="story-controls">
				<div
				  class="janrainSocialPlaceholder"
				  data-janrain-url="https://apple.slashdot.org/story/17/11/27/1840232/two-major-cydia-hosts-shut-down-as-jailbreaking-fades-in-popularity"
				  data-janrain-title="Two Major Cydia Hosts Shut Down as Jailbreaking Fades in Popularity"
				  data-janrain-message="Two Major Cydia Hosts Shut Down as Jailbreaking Fades in Popularity @slashdot"
				></div>




			</div>


				<div class="story-tags">
					<span class="tright tags"><menu type="toolbar" class="edit-bar">
		<span id="tagbar-95536639" class="tag-bar none">
			<a  class="topic tag" rel="statictag" href="//slashdot.org/tag/" target="_blank"></a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/business" target="_blank">business</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/iphone" target="_blank">iphone</a>
<a  class="popular tag" rel="statictag" href="//slashdot.org/tag/it" target="_blank">it</a>

		</span>

			<a class="edit-toggle" href="/my/login/" onclick="show_login_box();return false;">
				<span class="icon-tag btn collapse"></span>
			</a>


		<div class="tag-menu">
			<input class="tag-entry default" type="text" value="apply tags">
		</div>





	</menu></span>
				</div>


		</footer>




	</article>
				</div>

				<!-- LOWER PAGINATION -->
				<div class="row">
					<div class="paginate" id="fh-pag-div">
<div class="menu2" id="fh-paginate">






	 <a class="prevnextbutdis" href="#" onclick="return false;">&laquo; Newer</a>


		<a class="prevnextbutact" href="//slashdot.org/?page=1" >Older &raquo;</a>

	<span class="inactive more">

	</span>





</div>
</div>
				</div>

				<!-- WIT -->
				<span id="itemsreturned" class="row">

				</span>


				<!-- index2_variant |A|-->


				<div class="row">
				</div>



				<!-- Taboola: below articles widget -->
<div class="row">
	<div id="taboola-below-article-thumbnails-2nd"></div>
	<script type="text/javascript">
		window._taboola = window._taboola || [];
		_taboola.push({
			mode: 'thumbnails-b',
			container: 'taboola-below-article-thumbnails-2nd',
			placement: 'Below Article Thumbnails 2nd',
			target_type: 'mix'
		});
	</script>
</div>

				<!-- Slashdot Deals 6 Best Sellers -->
				<div class="row">
					<div class="deals-wrapper">
					  <div class="deals-header"><h1>Slashdot Top Deals</h1></div>
					  <div id="deals-output">
						<script id="deals-template" type="text/x-handlebars-template">
						  {{#each deal}}
							<div class="deal">
							  <a href="{{urlPath permalink}}?&utm_source=slashdot.org&utm_medium=dealfeed-footerfeed&utm_campaign={{slug}}" target="_blank">
							  	<img src="{{main_image}}" alt="" />
							  </a>
							  <p class="title"><a href="{{urlPath permalink}}?&utm_source=slashdot.org&utm_medium=dealfeed-footerfeed&utm_campaign={{slug}}" target="_blank">{{title}}</a></p>
							  <p class="deal-price">{{centConversion price_in_cents}}</p>
							</div>
						  {{/each}}
						</script>
					  </div>
					</div>
				</div>
				<script>
					if ( isAdBlockActive ) {
						$.getScript( "//a.fsdn.com/sd/js/scripts/min/deals-min.js", function(){
							runDealsWidget();
						});
					}
				</script>

			<!-- End Slashdot Deals 6 Best Sellers -->

				<!-- SLASH-4560 NEW AD HERE (dhand) -->
				<div id="bottomadspace">
					<table id="bottomadtable">
						<tr>
							<td><div id='div-gpt-ad-728x90_b'><script type='text/javascript'>
googletag.cmd.push(function(){
googletag.display('div-gpt-ad-728x90_b');});</script></div></td>
						</tr>
					</table>
				</div>
			</div>
		</div>
	</div>


	<aside id="slashboxes" class="rail-right scroll-fixable">


		   <div class="advertisement railad adwrap-unviewed">
<div id='div-gpt-ad-300x250_a'><script type='text/javascript'>
googletag.cmd.push(function(){
googletag.display('div-gpt-ad-300x250_a');});</script></div>
</div>


		<article class="deals-rail">
		  <header id="slashdot_deals-title"><h2>Slashdot Top Deals</h2></header>
		  <div id="deals-rail-output">
			<script id="deals-rail-template" type="text/x-handlebars-template">
				{{#each deal}}
					<div class="">
					  <a href="{{urlPath permalink}}?&utm_source=slashdot.org&utm_medium=dealfeed-righthand&utm_campaign={{slug}}" target="_blank">
					  	<img src="{{main_image}}" alt="" />
					  </a>
					  <div class="deal-overlay">
						  <div class="title"><a href="{{urlPath permalink}}?&utm_source=slashdot.org&utm_medium=dealfeed-righthand&utm_campaign={{slug}}" target="_blank">{{title}}</a></div>
						  <div class="deal-price">{{centConversion price_in_cents}}</div>
						</div>
					</div>
				{{/each}}
			</script>
		  </div>
		</article>

		<!-- Newsletter image -->
		<div class="ad-blocked-newsletter">
			<a href="//slashdot.org/newsletter" target="_blank"><img src="//a.fsdn.com/sd/NewsletterSubscription.png" alt="" /></a>
		</div>





			<script type="text/javascript">
				$(function() {
					// Poll/Pulse
					(function(){
						var sd_poll = $('#poll'),
								pulsead = $('#div-gpt-ad-pulse_300x600_a');

						sd_poll.hide();

						function showSdPoll(){
							if( pulsead.closest('.advertisement').height() < 250 ) {
								sd_poll.fadeIn();
								pulsead.closest('.advertisement').hide();
							}
						}
						//this function will display the Slashdot Poll if the Pulse Ad is not delivered
						setTimeout(function() { showSdPoll(); }, 2000);
					})();
				});
			</script>
			<div id='my_forgebox'>

			</div>



					<article id="slashdot_deals" class="nosort">
		<header id="slashdot_deals-title">
			<h2><a href="http://deals.slashdot.org/">Slashdot Deals</a></h2>
		</header>
		<section class="b" id="slashdot_deals-content">
			<script type='text/javascript'>
googletag.cmd.push(function()
{ googletag.defineSlot('/7346874/sld-300x250', [300, 250], 'div-gpt-ad-1435005138111-0').addService(googletag.pubads()); googletag.pubads().enableSingleRequest(); googletag.enableServices(); }
);
</script>
<div id='div-gpt-ad-1435005138111-0' style='height:250px; width:300px;'>
<script type='text/javascript'>
googletag.cmd.push(function()
{ googletag.display('div-gpt-ad-1435005138111-0'); }
);
</script>

</div>

		</section>
	</article><div class="railad advertisement">
<div id='div-gpt-ad-300x250_b'><script type='text/javascript'>
googletag.cmd.push(function(){
googletag.display('div-gpt-ad-300x250_b');});</script></div>
</div><article class="nosort">
	<header id="poll-title">
		<h2>Slashdot Poll</h2>
	</header>
	<section class="b" id="poll-content">
		<style>
		.poll-voted { display: none; }
	</style>

		<div class="units-6 poll-group-form">

				<h3>What's your favorite laptop brand/type?</h3>

			<h3 class="output"></h3>
			<form id="pollBooth" action="//slashdot.org/pollBooth.pl" method="post">
				<input type="hidden" name="qid" value="3061">

					<input type="hidden" name="section" value="slashdot">


						<label>
							<input type="radio" name="aid" value="1">
							Apple
						</label>

						<label>
							<input type="radio" name="aid" value="2">
							Chromebook
						</label>

						<label>
							<input type="radio" name="aid" value="3">
							Dell
						</label>

						<label>
							<input type="radio" name="aid" value="4">
							HP
						</label>

						<label>
							<input type="radio" name="aid" value="5">
							Lenovo
						</label>

						<label>
							<input type="radio" name="aid" value="6">
							Microsoft
						</label>

						<label>
							<input type="radio" name="aid" value="7">
							Toshiba
						</label>

						<label>
							<input type="radio" name="aid" value="8">
							Other (specify in comments)
						</label>

					<div class="poll-controls">
						<button type="submit" class="btn-polls">vote now</button>

					</div>
					<footer>
						<span>
							<a href="/poll/3061/whats-your-favorite-laptop-brandtype">Read the <strong>287</strong> comments </a> |
							<strong>17308</strong> votes
						</span>
					</footer>
			</form>
		</div>
		<div class="units-6 poll-results-inline">
			<h3 id="message-completed-poll">

					Looks like someone has already voted from this IP. If you would like to vote please login and try again.

			</h3>

				<h3>What's your favorite laptop brand/type?</h3>

			<div class="doughnut-chart-wrapper">
				<div class="doughnut-chart" data-percent="0"><span>0</span></div>
				<div class="doughnut-chart-label">
					<span>Percentage of others that also voted for:</span>
					<h3></h3>
				</div>
			</div>

			<div class="poll-controls">
				<ul class="poll-options">
					<li>
						<a href="/poll/3061/whats-your-favorite-laptop-brandtype" class="btn-polls">view results</a>
					</li>
					<li class="poll-choice"> Or <li>
					<li>
						<a href="//slashdot.org/polls" class="btn-polls">view more</a>
						<input type="hidden" id="reskey" name="reskey" value="v9KNJt2rwSrlBlMRCiKg">
					</li>
				</ul>
			</div>
			<footer>
				<span>
					<a href="/poll/3061/whats-your-favorite-laptop-brandtype">Read the <strong>287</strong> comments </a> |
					<strong>17308</strong> voted
				</span>
			</footer>
		</div>
	</section>
</article><div class="railad advertisement">
<div id='div-gpt-ad-300x250_c'><script type='text/javascript'>
googletag.cmd.push(function(){
googletag.display('div-gpt-ad-300x250_c');});</script></div>
</div><div id="taboola-below-main-column-thumbnails"></div>
<script type="text/javascript">
  if ( 1 || isAdBlockActive ) {
      window._taboola = window._taboola || [];
      _taboola.push({
        mode: 'thumbnails-rr3',
        container: 'taboola-below-main-column-thumbnails',
        placement: 'Below Main Column Thumbnails',
        target_type: 'mix'
      });
  };
</script><article class="nosort">
	<header id="mostdiscussed-title">
		<h2>Most Discussed</h2>
	</header>
	<section class="b" id="mostdiscussed-content">
		<ul id="mostdiscussed">


<li>
<span class="cmntcnt"><span class="slant"></span><span >534<span class="hide"> comments</span></span></span>
 <a href="//developers.slashdot.org/story/17/11/27/039226/why-esr-hates-c-respects-java-and-thinks-go-but-not-rust-will-replace-c?sbsrc=md">Why ESR Hates C++, Respects Java, and Thinks Go (But Not Rust) Will Replace C</a>
</li>


<li>
<span class="cmntcnt"><span class="slant"></span><span >380<span class="hide"> comments</span></span></span>
 <a href="//news.slashdot.org/story/17/11/27/0420208/could-collapsing-antarctic-glaciers-raise-sea-levels-sooner-than-expected?sbsrc=md">Could Collapsing Antarctic Glaciers Raise Sea Levels Sooner Than Expected?</a>
</li>


<li>
<span class="cmntcnt"><span class="slant"></span><span >253<span class="hide"> comments</span></span></span>
 <a href="//science.slashdot.org/story/17/11/26/2143200/big-tobacco-loses-11-year-fight-forced-to-broadcast-dangers-of-smoking-ads?sbsrc=md">Big Tobacco Loses 11-Year Fight, Forced To Broadcast 'Dangers of Smoking' Ads</a>
</li>


<li>
<span class="cmntcnt"><span class="slant"></span><span >238<span class="hide"> comments</span></span></span>
 <a href="//news.slashdot.org/story/17/11/26/0334211/taking-the-profit-out-of-killing-net-neutrality?sbsrc=md">Taking The Profit Out Of Killing 'Net Neutrality'</a>
</li>


<li>
<span class="cmntcnt"><span class="slant"></span><span >237<span class="hide"> comments</span></span></span>
 <a href="//yro.slashdot.org/story/17/11/27/0821232/tim-wu-why-the-courts-will-have-to-save-net-neutrality?sbsrc=md">Tim Wu: Why the Courts Will Have to Save Net Neutrality</a>
</li>

</ul>
	</section>
</article><article class="nosort">
	<header id="srandblock-title">
		<h2><a href="//slashdot.org/recent/">Firehose</a></h2>
	</header>
	<section class="b" id="srandblock-content">
		<ul>
<li>


	<a href="//slashdot.org/submission/7650659/the-guardian-newspaper-asks-readers-for-support-and-it-works?utm_source=rss1.0&amp;utm_medium=feed&amp;sbsrc=firehose">
		The Guardian newspaper asks readers for support, and it works
	</a>
</li><li>


	<a href="//slashdot.org/submission/7648865/understanding-the-red-hat---ibm---google---facebook-gpl-enforcement-announcement?utm_source=rss1.0&amp;utm_medium=feed&amp;sbsrc=firehose">
		Understanding the Red Hat - IBM - Google - Facebook GPL Enforcement Announcement
	</a>
</li><li>


	<a href="//slashdot.org/submission/7648751/drone-pilot-arrested-after-flying-over-two-stadiums-dropping-leaflets?utm_source=rss1.0&amp;utm_medium=feed&amp;sbsrc=firehose">
		Drone Pilot Arrested After Flying Over Two Stadiums, Dropping Leaflets
	</a>
</li><li>


	<a href="//slashdot.org/submission/7648747/mit-begfunding-campaign-will-bring-app-inventor-to-kids-with-1000-iphones?utm_source=rss1.0&amp;utm_medium=feed&amp;sbsrc=firehose">
		MIT Begfunding Campaign Will Bring App Inventor to Kids With $1,000 iPhones
	</a>
</li><li>


	<a href="//slashdot.org/submission/7648711/a-history-of-webassembly-from-one-of-the-developers?utm_source=rss1.0&amp;utm_medium=feed&amp;sbsrc=firehose">
		A history of WebAssembly, from one of the developers
	</a>
</li>
</ul>
	</section>
</article><article id="thisday" class="nosort">
		<header id="thisday-title">
			<h2><a href="">This Day on Slashdot</a></h2>
		</header>
		<section class="b" id="thisday-content">
			<table bgcolor="333333" class="thisday-tb"><tbody>


<tr>
	<td class="thisday-yr">
		2011
	</td>
	<td>
		<a href="//science.slashdot.org/story/11/11/28/0050228/muslim-medical-students-boycott-darwin-lectures?sbsrc=thisday">Muslim Medical Students Boycott Darwin Lectures</a>
	</td>
	<td>
	<span style="" class="cmntcnt"><span style="background:#333" class="slant"></span><span style="background: #333; color:#fff; font-weight:bold; font-size:.85em">1319<span class="hide"> comments</span></span></span>
	</td>
</tr>


<tr>
	<td class="thisday-yr">
		2010
	</td>
	<td>
		<a href="//yro.slashdot.org/story/10/11/28/1732205/wikileaks-under-denial-of-service-attack?sbsrc=thisday">WikiLeaks Under Denial of Service Attack</a>
	</td>
	<td>
	<span style="" class="cmntcnt"><span style="background:#333" class="slant"></span><span style="background: #333; color:#fff; font-weight:bold; font-size:.85em">870<span class="hide"> comments</span></span></span>
	</td>
</tr>


<tr>
	<td class="thisday-yr">
		2008
	</td>
	<td>
		<a href="//ask.slashdot.org/story/08/11/28/2015206/would-you-add-easter-eggs-to-software-produced-at-work?sbsrc=thisday">Would You Add Easter Eggs To Software Produced At Work?</a>
	</td>
	<td>
	<span style="" class="cmntcnt"><span style="background:#333" class="slant"></span><span style="background: #333; color:#fff; font-weight:bold; font-size:.85em">747<span class="hide"> comments</span></span></span>
	</td>
</tr>


<tr>
	<td class="thisday-yr">
		2007
	</td>
	<td>
		<a href="//ask.slashdot.org/story/07/11/28/1823205/how-to-deal-with-stolen-code?sbsrc=thisday">How to Deal With Stolen Code?</a>
	</td>
	<td>
	<span style="" class="cmntcnt"><span style="background:#333" class="slant"></span><span style="background: #333; color:#fff; font-weight:bold; font-size:.85em">799<span class="hide"> comments</span></span></span>
	</td>
</tr>


<tr>
	<td class="thisday-yr">
		2006
	</td>
	<td>
		<a href="//politics.slashdot.org/story/06/11/28/1814245/newt-gingrich-says-free-speech-may-be-forfeit?sbsrc=thisday">Newt Gingrich Says Free Speech May Be Forfeit</a>
	</td>
	<td>
	<span style="" class="cmntcnt"><span style="background:#333" class="slant"></span><span style="background: #333; color:#fff; font-weight:bold; font-size:.85em">894<span class="hide"> comments</span></span></span>
	</td>
</tr>

</tbody></table>

		</section>
	</article><article id="sourceforge2" class="nosort">
		<header id="sourceforge2-title">
			<h2><a href="">Sourceforge Top Downloads</a></h2>
		</header>
		<section class="b" id="sourceforge2-content">
			<ul class="sf_widget">
    <li>
                <a onclick="trackLink(this, 'sfSlashboxDownloadLink', 'http://sourceforge.net/projects/vlc/?source=sd_slashbox');return false;" href="http://sourceforge.net/projects/vlc/?source=sd_slashbox">VLC Media Player<span class="sf-size">822M Downloads</span></a>
</li>
   <li>
                <a onclick="trackLink(this, 'sfSlashboxDownloadLink', 'http://sourceforge.net/projects/emule/?source=sd_slashbox');return false;" href="http://sourceforge.net/projects/emule/?source=sd_slashbox">eMule<span class="sf-size">683M Downloads</span></a>
   </li>
       <li>
                <a onclick="trackLink(this, 'sfSlashboxDownloadLink', 'http://sourceforge.net/projects/azureus/?source=sd_slashbox');return false;" href="http://sourceforge.net/projects/azureus/?source=sd_slashbox">Azureus/vuze<span class="sf-size">539M Downloads</span></a>
       </li>
        <li>
                <a onclick="trackLink(this, 'sfSlashboxDownloadLink', 'http://sourceforge.net/projects/aresgalaxy/?source=sd_slashbox');return false;" href="http://sourceforge.net/projects/aresgalaxy/?source=sd_slashbox">Ares Galaxy<span class="sf-size">338M Downloads</span></a>
   </li>
       <li>
                <a onclick="trackLink(this, 'sfSlashboxDownloadLink', 'href=" http:="" sourceforge.net="" projects="" corefonts="" ');return="" false;"="" href="http://sourceforge.net/projects/corefonts/?source=sd_slashbox">Microsoft core fonts<span class="sf-size">300M Downloads</span></a>
     </li>
</ul>
<div id="sf-logo">
       <p>Powered By</p>
      <a onclick="trackLink(this, 'sfSlashboxHomeLink', 'http://sourceforge.net/?source=sd_slashbox');return false;" href="http://sourceforge.net/?source=sd_slashbox">sf</a>
</div>

		</section>
	</article>
					<div class="advertisement railad">
<div id='div-gpt-ad-300x250_d'><script type='text/javascript'>
googletag.cmd.push(function(){
googletag.display('div-gpt-ad-300x250_d');});</script></div>
</div>






	</aside>
</div>

<script type="text/javascript">
	firehose_exists = 1;
	$(function(){
	$('#firehose-filter').focus(function(event){ gFocusedText = this; })
	.blur(function(event){
		if ( gFocusedText === this ) {
			gFocusedText = null;
		}
	});


	apply_updates_when(		'at-end', true);
});


					firehose_settings.startdate = "";
					firehose_settings.mode = "mixed";
					firehose_settings.fhfilter = "";
					firehose_settings.orderdir = "DESC";
					firehose_settings.orderby = "createtime";
					firehose_settings.duration = -1;
					firehose_settings.color = "green";
					firehose_settings.view = "stories";
					firehose_settings.viewtitle = "";
					firehose_settings.tab = "";
					firehose_settings.base_filter = "";
					firehose_settings.user_view_uid = "";
					firehose_settings.sectionname = "Main";

	firehose_settings.issue = "";
	firehose_settings.section = 13;
	$('#searchquery').val(firehose_settings.fhfilter);



    fh_is_admin = 0;

	firehose_sitename = "Slashdot";
	firehose_slogan = "News for nerds, stuff that matters";
    if (fh_is_admin) {
	   firehose_update_title_count();
    }
	firehose_smallscreen = 0;





		firehose_settings.index = 1;




	var firehose_action_time = 0;
	var firehose_user_class = 0;



	var fh_color = "green";
	fh_colors = [ "red", "orange", "yellow", "green", "blue", "indigo", "violet", "black" ];
	var fh_colors_hash = new Array(0);
	for (var i=0; i< fh_colors.length; i++) {
		fh_colors_hash[fh_colors[i]] = i;
	}

	var fh_view_mode = "mixed";
	firehose_settings.page = 0;

	fh_is_admin = 0;
	var updateIntervalType = 2;
	var inactivity_timeout = 3600;
	setFirehoseAction();
	var update_time = "2017-11-28 10:37:02";

	var maxtime = "2017-11-28 10:37:02";
	var insert_new_at = "top";



fh_ticksize = 15;
sitename = 'idle.slashdot.org';





</script><!-- footer type=current begin -->

	</section>




	<footer id="fhft" class="grid_24 nf">
		<div id="logo_nf" class="fleft">
			<a href="//slashdot.org"><span>Slashdot</span></a>
		</div>
		<nav role="firehose footer">



				<ul id="pagination-controls">


						<li class="fleft">
							<a href="//slashdot.org/?issue=20171128">Today</a>
						</li>


						<li class="fleft">
							<a href="//slashdot.org/?issue=20171127">Monday</a>
						</li>


						<li class="fleft">
							<a href="//slashdot.org/?issue=20171126">Sunday</a>
						</li>


						<li class="fleft">
							<a href="//slashdot.org/?issue=20171125">Saturday</a>
						</li>


						<li class="fleft">
							<a href="//slashdot.org/?issue=20171124">Friday</a>
						</li>


						<li class="fleft">
							<a href="//slashdot.org/?issue=20171123">Thursday</a>
						</li>


						<li class="fleft">
							<a href="//slashdot.org/?issue=20171122">Wednesday</a>
						</li>


						<li class="fleft">
							<a href="//slashdot.org/?issue=20171121">Tuesday</a>
						</li>

				</ul>
				<script> /* fh_pag_update() */</script>

			<ul class="fright submitstory">
					<li class="fright">
						<a href="/submit">Submit<span class="opt"> Story</span></a>
					</li>
			</ul>
		</nav>



	</footer>
	<section class="bq">
		<blockquote class="msg grid_24" cite="https://slashdot.org">
			<p>Keep the number of passes in a compiler to a minimum.
		-- D. Gries</p>
			<span class="slant"></span>
		</blockquote>
	</section>
	<footer id="ft" class="grid_24">
		<nav class="grid_10" role="footer">
			<ul>
				<li><a href="//slashdot.org/faq">FAQ</a></li>
				<li><a href="//slashdot.org/archive.pl">Story Archive</a></li>
				<li><a href="//slashdot.org/hof.shtml">Hall of Fame</a></li>
				<li><a href="http://slashdotmedia.com/advertising-and-marketing-services/">Advertising</a></li>
				<li><a href="http://slashdotmedia.com/terms-of-use/">Terms</a></li>
				<li><a href="http://slashdotmedia.com/privacy-statement/">Privacy</a></li>
				<li id="teconsent"></li>
				<li><a href="http://slashdotmedia.com/opt-out-choices/">Opt Out Choices</a></li>
				<li><a href="//slashdot.org/faq/slashmeta.shtml">About</a></li>
				<li><a href="mailto:feedback@slashdot.org">Feedback</a></li>
				<li><a href="#" onclick="set_mobile_pref('mobile',1);return false;">Mobile View</a></li>
				<li><a href="//slashdot.org/blog">Blog</a></li>
			</ul>
		</nav>
		<br>

		<div class="grid_14 tright tm">Trademarks property of their respective owners. Comments owned by the poster. <span class="nobr">Copyright &copy; 2017 SlashdotMedia. All Rights Reserved.</span></div>
                <script type="text/javascript" src="//consent-st.truste.com/get?name=notice.js&amp;domain=slashdot.org&amp;c=teconsent&amp;text=true"></script>
	</footer>


	<div class="overlay"></div>
<div class="modal-box">
    <a href="#" id="close-modal">Close</a>
    <article class="modal-content">
    </article>
    <footer>
</div>




<div id="modal_cover" class="hide" onclick="hide_modal_box(); return false;"></div>
<div id="modal_box" class="hide">
      <div id="modal_box_content"></div>
      <header class="n">
                  <span class="fadeout"></span>
                  <span class="fadeoutfade"></span>
		  <span class="pf"><a class="ico close" onclick="hide_modal_box(); return false;" href="#"><span>Close</span></a></span>
		  <h3 class="pf"><div id="logo"><a href="//slashdot.org">Slashdot</a></div><span id="preference_title"></span></h3>
      </header>
</div>

	<!-- CCM Tag -->
<script type="text/javascript">
  (function () {
    /*global _ml:true, window */
    _ml = window._ml || {};
    _ml.eid = '771';

    var s = document.getElementsByTagName('script')[0], cd = new Date(), mltag = document.createElement('script');
    mltag.type = 'text/javascript'; mltag.async = true;
    mltag.src = '//ml314.com/tag.aspx?' + cd.getDate() + cd.getMonth() + cd.getFullYear();
    s.parentNode.insertBefore(mltag, s);
  })();
</script>
<!-- End CCM Tag -->

<script type="text/javascript">
window.google_analytics_uacct = "UA-32013-5";

var _gaq = _gaq || [];





  _gaq.push(['_setAccount', 'UA-36136016-1']);
  _gaq.push(['b._setAccount', 'UA-32013-5']);
  _gaq.push(['_setDomainName', '.slashdot.org']);
  _gaq.push(['b._setDomainName', '.slashdot.org']);


		_gaq.push(['_addIgnoredRef', 'slashdot.org']);
		_gaq.push(['b._addIgnoredRef', 'slashdot.org']);



  _gaq.push(['_setCustomVar', 1, 'User Type',  'Anon', 3]);
  _gaq.push(['b._setCustomVar', 1, 'User Type',  'Anon', 3]);

	_gaq.push(['_setCustomVar', 2, 'Page','index2', 3]);
	_gaq.push(['b._setCustomVar', 2, 'Page','index2', 3]);





// track beta behavior for user
var betamatches = document.cookie.match(/betagroup=(-?\d+)/);

if(betamatches && betamatches[1]) {
  if(betamatches[1] == -1) {
    _gaq.push(['_setCustomVar', 3, 'Beta-Usage','opt-out', 3]);
  } else {
    _gaq.push(['_setCustomVar', 3, 'Beta-Usage','unredirected', 3]);
  }
}



  _gaq.push(['_trackPageview']);
  _gaq.push(['b._trackPageview']);
  _gaq.push(['_trackPageLoadTime']);
  _gaq.push(['b._trackPageLoadTime']);




  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

<!-- CCM GA Push -->
<script>
    if (typeof _ml !== 'undefined' && _ml.us) {
        if (_ml.us.tp && _ml.us.tp.length > 0) {
            ga('set', 'dimension2', _ml.us.tp[0]);
        }
        if (_ml.us.pc && _ml.us.pc.length > 0) {
            ga('set', 'dimension7', _ml.us.pc[0]);
        }
        ga('set', 'dimension3', _ml.us.ind);
        ga('set', 'dimension4', _ml.us.cr);
        ga('set', 'dimension5', _ml.us.cs);
        ga('set', 'dimension6', _ml.us.dm);
        ga('set', 'dimension8', _ml.us.sn);
    }
</script>

<!-- Sticky Ads -->
<script type="text/javascript">
var topBannerViewed = false;
if($('#div-gpt-ad-728x90_a').length > 0 && window.outerWidth >= 1070 && !isAdBlockActive){
    $(window).scroll(function(){
        var y = $(document).scrollTop();
        var z =  y + window.outerHeight;
        var navOffset = 0;
        var offset = [
            $('.nav-wrap').outerHeight(true),
            $('.nav-secondary-wrap').outerHeight(true)
        ];
        for(row in offset){
            if(offset[row]) navOffset = navOffset + parseInt(offset[row]);
        }
        $('.adwrap-unviewed').each(function(){
            var cls = 'adwrap-sticky';
            var toggleCls = 'adwrap';
			$('.banner-wrapper').css('height', $('.banner-contain').outerHeight());
            if($(this).hasClass('railad')) {
                if(topBannerViewed){
                    var topPixels = $(this).offset().top;
                    navOffset += $('.adwrap').outerHeight();
                    if(y >= topPixels && y >= navOffset){
                        $('#slashboxes').css('top', 0).css('position','fixed').css('right',13);
                    } else {
                        $('#slashboxes').removeAttr('style');
                    }
                }
                return;
            }
            var topPixels = $(this).offset().top;
            if(y >= topPixels && y >= navOffset){
                $(this).addClass(cls);
                $(this).removeClass('adwrap');
				if(cls == 'adwrap-sticky') { //top banner
                    topBannerViewed = false;
					$('#slashboxes').css('top',$(this).outerHeight() || 0).css('position','fixed').css('right',13);
				}
                if(topBannerViewed) {
                    console.log('hereeee');
					$('#slashboxes').css('top', 0).css('position','fixed').css('right',13);
				}
            }else{
                $(this).removeClass(cls);
                $(this).addClass(toggleCls);
                $('#slashboxes').removeAttr('style');
            }
        });
		if($('.adwrap-viewed-banner').length > 0){
			topBannerViewed = true;
			$('.adwrap-viewed-banner').removeClass('adwrap-unviewed').removeClass('adwrap-sticky').addClass('adwrap');
		}
        if($('.adwrap-viewed-railad').length > 0){
            $('.adwrap-viewed-railad').removeClass('adwrap-unviewed').removeClass('adwrap-railad-sticky');
			$('#slashboxes').removeAttr('style');
		}
    });
}
</script>

<!-- Piwik -->
<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(["setCookieDomain", "*.slashdot.org"]);
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//analytics.slashdotmedia.com/";
    _paq.push(['setTrackerUrl', u+'sd.php']);
    _paq.push(['setSiteId', 40]);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'sd.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<noscript><p><img src="//analytics.slashdotmedia.com/sd.php?idsite=40" style="border:0;" alt="" /></p></noscript>

<!-- Sponsored Whitepaper/Documents -->
<script>
    if(window.location.pathname == '/'){
        var nelId = (location.search.split('nel_id=')[1] || '').split('&')[0];
        var url = '/ajax.pl?op=nel';
        if(nelId){
            url += '&nel_id='+nelId;
        }
        $.ajax({
            url: url,
            success: function(html){
                $('#firehoselist article').eq(1).after(html);
            }
        });

        $.ajax({
            url: '/ajax.pl?op=geo',
            success: function(geo){
                var text = "";
                var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
                for( var i=0; i < 15; i++ )
                        text += possible.charAt(Math.floor(Math.random() * possible.length));
                window.addEventListener('message', receiveMessage, false);
                function receiveMessage(evt){
                    if (evt.data && evt.data.lf_iframeid && evt.data.lf_height) {
                        //resize iframe to fit larger leadgen form
                        document.getElementById(evt.data.lf_iframeid).height = (evt.data.lf_height) + "px";
                    }
                }
                $('#firehoselist article').eq(12).after('<iframe width="100%" height="0" scrolling="no" frameborder="0" id="bz-lf-'+text+'" name="bz-lf-'+text+'" src="//d1o5u7ifbz3swt.cloudfront.net/showcase/index.php?id=dynamic&lp=SD_IMM&country='+geo+'"></iframe>');
            }
        });
    }
</script>

<script type="text/javascript">
_linkedin_data_partner_id = "113712";
</script><script type="text/javascript">
(function(){var s = document.getElementsByTagName("script")[0];
var b = document.createElement("script");
b.type = "text/javascript";b.async = true;
b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
s.parentNode.insertBefore(b, s);})();
</script>
<noscript>
<img height="1" width="1" style="display:none;" alt="" src="https://dc.ads.linkedin.com/collect/?pid=113712&fmt=gif" />
</noscript>

<!-- Datonics -->
<script async type="text/javascript" src="//ads.pro-market.net/ads/scripts/site-143573.js"></script>
	<script id="after-content" type="text/javascript">
(function( $, fn, console ){
	$ && fn && $(function(){ fn($, console); });
})(window.jQuery, window.pageload_done, window.console);
</script>

	<script type='text/javascript'>
	if(!document.location.href.match(/source=autorefresh/)) {
		document.write('<img src="//slashdot.org/images/js.gif?777">');
	}
</script>
<noscript>
	<img src="//slashdot.org/images/njs.gif?671">
</noscript>
	<div class="busy genericspinner hide"><span>Working...</span></div>
	<script>
		if(typeof(Storage)!=="undefined"){
			window.scrollTo(0,sessionStorage.scrollPos);
				$(window).scroll(function () {
				//You've scrolled this much:
				sessionStorage.scrollPos = $(window).scrollTop();
			});
		}
		$(function(){
			$('a').click(function(){
				delete sessionStorage.scrollPos;
			})
		});
		// window.onbeforeunload = function () {
		// 	console.log('bakc button clicked');
		// 	delete sessionStorage.scrollPos;
		// }
		window.onpopstate=function() {
			delete sessionStorage.scrollPos;
		}
	</script>



		<!-- 1x1 home page -->
		<div id='div-gpt-ad-1x1'><script type='text/javascript'>
googletag.cmd.push(function(){
googletag.display('div-gpt-ad-1x1');});</script></div>


        <script type="text/javascript">
          window._taboola = window._taboola || [];
          _taboola.push({flush: true});
        </script>

	</body>
	</html>


	<!-- footer type=current end -->
"""



def main():
    task(code*2)


if __name__ == "__main__":
    main()
