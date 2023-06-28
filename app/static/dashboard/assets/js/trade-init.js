(function ($) {
  new TradingView.widget({
    width: "100%",
    height: 500,
    symbol: "NASDAQ:AAPL",
    interval: "D",
    timezone: "exchange",
    theme: "light",
    style: "1",
    toolbar_bg: "#f1f3f6",
    withdateranges: true,
    allow_symbol_change: true,
    save_image: true,
    details: false,
    hotlist: false,
    calendar: false,
    enable_publishing: false,
    withdateranges: true,
    hide_side_toolbar: false,
    allow_symbol_change: true,
    show_popup_button: true,
    locale: "en",
    container_id: "tradingview_e8053",
  });
  new PerfectScrollbar("#market-news");
})(jQuery);
