header = """
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
        <meta charset="utf-8"> <!-- utf-8 works for most cases -->
        <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
        <meta name="x-apple-disable-message-reformatting">  <!-- Disable auto-scale in iOS 10 Mail entirely -->
        <title></title> <!-- The title tag shows in email notifications, like Android 4.4. -->

        <link href="https://fonts.googleapis.com/css?family=Work+Sans:200,300,400,500,600,700" rel="stylesheet">

        <!-- CSS Reset : BEGIN -->
        <style>

            /* What it does: Remove spaces around the email design added by some email clients. */
            /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
            html,
    body {
        margin: 0 auto !important;
        padding: 0 !important;
        height: 100% !important;
        width: 100% !important;
        background: #f1f1f1;
    }

    /* What it does: Stops email clients resizing small text. */
    * {
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%;
    }

    /* What it does: Centers email on Android 4.4 */
    div[style*="margin: 16px 0"] {
        margin: 0 !important;
    }

    /* What it does: Stops Outlook from adding extra spacing to tables. */
    table,
    td {
        mso-table-lspace: 0pt !important;
        mso-table-rspace: 0pt !important;
    }

    /* What it does: Fixes webkit padding issue. */
    table {
        border-spacing: 0 !important;
        border-collapse: collapse !important;
        table-layout: fixed !important;
        margin: 0 auto !important;
    }

    /* What it does: Uses a better rendering method when resizing images in IE. */
    img {
        -ms-interpolation-mode:bicubic;
    }

    /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
    a {
        text-decoration: none;
    }

    /* What it does: A work-around for email clients meddling in triggered links. */
    *[x-apple-data-detectors],  /* iOS */
    .unstyle-auto-detected-links *,
    .aBn {
        border-bottom: 0 !important;
        cursor: default !important;
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
    }

    /* What it does: Prevents Gmail from displaying a download button on large, non-linked images. */
    .a6S {
        display: none !important;
        opacity: 0.01 !important;
    }

    /* What it does: Prevents Gmail from changing the text color in conversation threads. */
    .im {
        color: inherit !important;
    }

    /* If the above doesn't work, add a .g-img class to any image in question. */
    img.g-img + div {
        display: none !important;
    }

    /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
    /* Create one of these media queries for each additional viewport size you'd like to fix */

    /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
    @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
        u ~ div .email-container {
            min-width: 320px !important;
        }
    }
    /* iPhone 6, 6S, 7, 8, and X */
    @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
        u ~ div .email-container {
            min-width: 375px !important;
        }
    }
    /* iPhone 6+, 7+, and 8+ */
    @media only screen and (min-device-width: 414px) {
        u ~ div .email-container {
            min-width: 414px !important;
        }
    }
        </style>

        <!-- CSS Reset : END -->

        <!-- Progressive Enhancements : BEGIN -->
        <style>

    	    .primary{
    	background: #17bebb;
    }
    .bg_white{
    	background: #ffffff;
    }
    .bg_light{
    	background: #d4e3e3;
    }
    .bg_black{
    	background: #000000;
    }
    .bg_dark{
    	background: rgba(0,0,0,.8);
    }
    .email-section{
    	padding:2.5em;
    }

    h1,h2,h3,h4,h5,h6{
    	font-family: 'Work Sans', sans-serif;
    	color: #000000;
    	margin-top: 0;
    	font-weight: 400;
    }

    body{
    	font-family: 'Work Sans', sans-serif;
    	font-weight: 400;
    	font-size: 15px;
    	line-height: 1.8;
    	color: rgba(0,0,0,.4);
    }

    a{
    	color: #17bebb;
    }

    table{
    }
    /*LOGO*/

    .logo h1{
    	margin: 0;
    }
    .logo h1 a{
    	color: #17bebb;
    	font-size: 24px;
    	font-weight: 700;
    	font-family: 'Work Sans', sans-serif;
    }

    /*HERO*/
    .hero{
    	position: relative;
    	z-index: 0;
    }

    .hero .text{
    	color: rgba(0,0,0,.3);
    }
    .hero .text h2{
    	color: #000;
    	font-size: 34px;
    	margin-bottom: 15px;
    	font-weight: 300;
    	line-height: 1.2;
    }
    .hero .text h4{
    	font-size: 18px;
    	font-weight: 200;
    }
    .hero .text h2 span{
    	font-weight: 600;
    	color: #000;
    }


    /*PRODUCT*/
    .product-entry{
    	display: block;
    	position: relative;
    	float: left;
    	padding-top: 20px;
    }
    .product-entry .text{
    	width: calc(100% - 125px);
    	padding-left: 20px;
    }
    .product-entry .text h4{
    	margin-bottom: 0;
    	padding-bottom: 0;
    }
    .product-entry .text p{
    	margin-top: 0;
    }
    .product-entry img, .product-entry .text{
    	float: left;
    }

    ul.social{
    	padding: 0;
    }
    ul.social li{
    	display: inline-block;
    	margin-right: 10px;
    }

    /*FOOTER*/

    .footer{
    	border-top: 1px solid rgba(0,0,0,.05);
    	color: rgba(0,0,0,.5);
    }
    .footer .heading{
    	color: #000;
    	font-size: 20px;
    }
    .footer ul{
    	margin: 0;
    	padding: 0;
    }
    .footer ul li{
    	list-style: none;
    	margin-bottom: 10px;
    }
    .footer ul li a{
    	color: rgba(0,0,0,1);
    }


    @media screen and (max-width: 500px) {


    }


        </style>


    </head>"""

body="""
    <body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #f1f1f1;">
    	<center style="width: 100%; background-color: #f1f1f1;">
        <div style="display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
          &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        </div>
        <div style="max-width: 600px; margin: 0 auto;" class="email-container">
        	<!-- BEGIN BODY -->
          <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
          	<tr>
              <td valign="top" class="bg_white" style="padding: 1em 2.5em 0 2.5em;">
              	<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
              		<tr>
              			<td class="logo" style="text-align: left;">
    			            <h1><a href="#">Dzień dobry!</a></h1>
    			          </td>
              		</tr>
              	</table>
              </td>
    	      </tr><!-- end tr -->
    				<tr>
              <td valign="middle" class="hero bg_white" style="padding: 1em 0 1em 0;">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                	<tr>
                		<td style="padding: 0 2.5em; text-align: left;">
                			<div class="text">
                				<h4>Dziś mamy {} ({}). <p> Imieniny obchodzą: <i> {} </i> <p> A ponadto...</h4>
                			</div>
                		</td>
                	</tr>
                </table>
              </td>
              
    	      </tr><!-- end tr -->
    	      <tr>
    	      	<table class="bg_white" role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
    					  <tr style="border-bottom: 1px solid rgba(0,0,0,.05);">
    					  		<td valign="middle" style="text-align:left; padding: 0 2.5em;" width = "20%"><img src="{}" width="100%" height="100%"</td>
    							<td width = "80%"> <h4><b> Pogoda </b></h4> 
    							<p>Temp max: {} C<p> Temp min: {} C<p>Wschód Słońca: {}<p> Zachód Słońca: {}</td>
    					  </tr>
    					   <tr style="border-bottom: 1px solid rgba(0,0,0,.05);">
    					  		<td valign="middle" style="text-align:left; padding: 0 2.5em;" width = "20%"><img src="https://img.redro.pl/plakaty/fajerwerki-wektorowa-ilustracja-na-bialym-tle-odosobniona-plaska-ikona-ilustracja-fajerwerki-z-nikt-400-149917096.jpg" width="100%" height="100%" </td>
    							<td width = "80%"> <h4><b> Święta </b></h4> <p>{}</td>
    					  </tr>
    					  <tr style="border-bottom: 1px solid rgba(0,0,0,.05);">
    					  		<td valign="middle" style="text-align:left; padding: 0 2.5em;" width = "20%"> <img src ="https://i.ibb.co/hRCfFCS/suchar.jpg" width="100%" height="100%" </td>
    							<td width = "80%"> <h4><b> Suchar dnia </b></h4> <p>{}</td>
    					  </tr>
    					  <tr style="border-bottom: 1px solid rgba(0,0,0,.05);">
    					  		<td valign="middle" style="text-align:left; padding: 0 2.5em;" width = "20%"> <img src ="https://media.istockphoto.com/vectors/white-star-on-red-circle-icon-or-symbol-vector-id1129175098?k=20&m=1129175098&s=170667a&w=0&h=8BWEFUtmeEAZ0anDtpVDtdqMQ3goJWWYuM2xpXAvLZ0=" width="100%" height="100%" </td>
    							<td width = "80%"> <h4><b> Najbliższe mecze Wisełki </b></h4> {}</td>
    					  </tr>

    	      	</table>
    	      </tr><!-- end tr -->
          <!-- 1 Column Text + Button : END -->
          </table>
          <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
          	<tr>
              <td valign="middle" class="bg_light footer email-section">
                <table>
                	<tr>
                    <td valign="top" width="66.666%" style="padding-top: 20px;">
                      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                        <tr>
                          <td style="text-align: left; padding-right: 10px;">
                          	<h3 class="heading">Angol na dziś</h3>
                          	<p>{}</p> 	

                          </td>
                        </tr>
                      </table>
                    </td>
                    <td valign="top" width="33.333%" style="padding-top: 20px;">
                      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                        <tr>
                          <td style="text-align: left; padding-left: 10px;">
                          	<h3 class="heading">Linki</h3>
                          	<ul>
    					                <li><a href="https://www.accuweather.com/pl/pl/dąbrowa/2663947/weather-forecast/2663947">Pogoda</a></li>
    					                <li><a href="https://news.google.com/topstories?hl=pl&gl=PL&ceid=PL:pl">Wiadomości</a></li>
    					                <li><a href="#">Kalendarium</a></li>
    					                <li><a href="https://www.wislaportal.pl">WislaPortal</a></li>
    					              </ul>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr><!-- end: tr -->
            <tr>
              <td class="bg_white" style="text-align: center;">
              	<p>Mail design by https://github.com/ColorlibHQ/</p>
              </td>
            </tr>
          </table>

        </div>
      </center>
    </body>
    </html>
    """