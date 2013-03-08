/**
 * @author Ivan.Lavriv
 */

var Elements = {
	registerWindow : '<div class="window_wrapper">'+
						'<div class="register_window reg">'+
							'<div class="top_form"><h3>Sign up for Web-science</h3><a onclick="GuiController.hideWindow();">×</a>'+
							'<div class="social_form">'+
							   '<a class="twitter">Sign Up with Twitter</a>'+
							   '<a class="facebook">Sign Up with Facebook</a>'+
							'</div>'+
							'<div class="email_login">'+
								'<div class="email_title">Or with email</div>'+
								'<input type="text" placeholder="Username"><br>'+
								'<input type="text" placeholder="Email">'+
								'<input type="password" placeholder="Password">'+
								'<input type="submit" value="Sign Up">'+
							'</div>'+
							'<div class="login_a"><a href="/login/"><span>Already have an account?</span> Log in</a></div>'+
							'</div>'+
						'</div>'+
					'</div>',
					
	loginWindow : '<div class="window_wrapper">'+
						'<div class="register_window log">'+
							'<div class="top_form"><h3>Log in to Web-science</h3><a onclick="GuiController.hideWindow();">×</a>'+
							'<div class="social_form">'+
							   '<a class="twitter">Log In with Twitter</a>'+
							   '<a class="facebook">Log In with Facebook</a>'+
							'</div>'+
							'<div class="email_login">'+
								'<div class="email_title">Or with web-science account</div>'+
								'<input type="text" placeholder="Username"><br>'+
								'<input type="password" placeholder="Password">'+
								'<input type="submit" value="Log In">'+
							'</div>'+
							'<div class="login_a log_a"><ul>'+
								'<li><a href="/login/"><span>Forgott password?</span></a></li>'+
								'<li><a href="/signup/"><span>Sign Up to web-sciense</span></a></li>'+
							'</ul></div>'+
						'</div>'+
					'</div>',
};

var GuiController = {
	showWindow : function () {
		var body = $('body');
	  	body.prepend(Elements.registerWindow);
	  	var wrapper = $('.window_wrapper');
	  	var registerWindow = $('.register_window');
	  	wrapper.animate({"opacity":1},200);
	  	registerWindow.animate({
	  		"margin-top":"40px"
	  	},400);
	},
	
	hideWindow : function () {	
	  var body = $('body');
	  var registerWindow = $('.register_window');
	  var wrapper = $('.window_wrapper');
	  wrapperLast = $('.window_wrapper:last');
	  if(wrapper.length == 2){
	 	 wrapperLast.remove();
	  }
	  registerWindow.animate({
	  "margin-top":"-500px"
	  },400);
	  wrapper.fadeOut(200);
	},
	
	loginWindow : function () {
		var body = $('body');
	  	body.prepend(Elements.loginWindow);
	  	var wrapper = $('.window_wrapper');
	  	var registerWindow = $('.register_window');
	  	wrapper.animate({"opacity":1},200);
	  	registerWindow.animate({
	  		"margin-top":"40px"
	  	},400);
	},
};