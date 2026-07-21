jQuery(function($) {

	$(function(){
		$('#main-slider.carousel').carousel({
			interval: 10000,
			pause: false
		});
	});

	//Ajax contact
	var form = $('.contact-form');
	form.submit(function () {
		$this = $(this);
		$.post($(this).attr('action'), function(data) {
			$this.prev().text(data.message).fadeIn().delay(3000).fadeOut();
		},'json');
		return false;
	});

	//smooth scroll
	$('.navbar-nav > li').click(function(event) {
		event.preventDefault();
		var target = $(this).find('>a').prop('hash');
		$('html, body').animate({
			scrollTop: $(target).offset().top
		}, 500);
	});

	//手机端菜单展开时给顶栏加实底，避免在页面顶端菜单透明看不清
	$('#navbar .navbar-collapse')
		.on('show.bs.collapse', function () {
			$(this).closest('.navbar-default').addClass('is-open');
		})
		.on('hidden.bs.collapse', function () {
			$(this).closest('.navbar-default').removeClass('is-open');
		});

	//scrollspy
	$('[data-spy="scroll"]').each(function () {
		var $spy = $(this).scrollspy('refresh')
	})

	//Isotope
	$(window).load(function(){
		$portfolio = $('.portfolio-items');
		$portfolio.isotope({
			itemSelector : 'li',
			layoutMode : 'fitRows'
		});
		$portfolio_selectors = $('.portfolio-filter >li>a');
		$portfolio_selectors.on('click', function(){
			$portfolio_selectors.removeClass('active');
			$(this).addClass('active');
			var selector = $(this).attr('data-filter');
			$portfolio.isotope({ filter: selector });
			return false;
		});
	});
});
/* 顶栏滚动渐显：滚到最顶部完全透明，下滑时白底与向下投影逐渐浮出。
   只在有顶栏的页面生效（目前只有 index.html）。 */
(function () {
	var nav = document.querySelector('#header .navbar-default');
	if (!nav || !window.requestAnimationFrame) return;

	var FADE = 140;   // 滚动多少像素后完全实底
	var ticking = false;

	function update() {
		var y = window.pageYOffset || document.documentElement.scrollTop || 0;
		nav.style.setProperty('--nav-p', Math.min(y / FADE, 1).toFixed(3));
		ticking = false;
	}

	window.addEventListener('scroll', function () {
		if (!ticking) {
			ticking = true;
			window.requestAnimationFrame(update);
		}
	}, { passive: true });

	update();   // 处理带 #anchor 载入或刷新时already-scrolled 的情况
})();

/* 首屏遮罩：滚到最顶部完全透明，下滑时渐变遮罩逐渐加深。
   只在有首屏的页面生效（目前只有 index.html）。 */
(function () {
	var hero = document.getElementById('main-slider');
	if (!hero || !window.requestAnimationFrame) return;

	var ticking = false;

	function update() {
		var y = window.pageYOffset || document.documentElement.scrollTop || 0;
		var span = (hero.offsetHeight || window.innerHeight) * 0.6;   // 滚过首屏 60% 时最深
		hero.style.setProperty('--scrim', span > 0 ? Math.min(y / span, 1).toFixed(3) : '0');
		ticking = false;
	}

	function onScroll() {
		if (!ticking) {
			ticking = true;
			window.requestAnimationFrame(update);
		}
	}

	window.addEventListener('scroll', onScroll, { passive: true });
	window.addEventListener('resize', onScroll, { passive: true });
	update();   // 处理带 #anchor 载入或刷新时 already-scrolled 的情况
})();
