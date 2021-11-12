$.noConflict();
jQuery(document).ready(function ($) {

    function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    $.ajax({
        type: 'GET',
        url: "/coinbase_btc",
        success: function (data) {
            var prices = data
            var $coin_buy_btc_price = $('#coin_buy_btc_price');
            var $coin_sell_btc_price = $('#coin_sell_btc_price');

            $coin_buy_btc_price.text("$" + numberWithCommas(prices.buy_price));
            $coin_sell_btc_price.text("$" + numberWithCommas(prices.sell_price));
        }
    });

    $.ajax({
        type: 'GET',
        url: "/coinbase_eth",
        success: function (data) {
            var prices = data
            var $coin_buy_eth_price = $('#coin_buy_eth_price');
            var $coin_sell_eth_price = $('#coin_sell_eth_price');

            $coin_buy_eth_price.text("$" + numberWithCommas(prices.buy_price));
            $coin_sell_eth_price.text("$" + numberWithCommas(prices.sell_price));
        }
    });

    $.ajax({
        type: 'GET',
        url: "/binance_btc",
        success: function (data) {
            var prices = data
            var $bin_buy_btc_price = $('#bin_buy_btc_price');
            var $bin_sell_btc_price = $('#bin_sell_btc_price');

            $bin_buy_btc_price.text("$" + parseFloat(prices.askPrice).toLocaleString("en-US", { maximumFractionDigits: 2, minimumFractionDigits: 2 }));
            $bin_sell_btc_price.text("$" + parseFloat(prices.lastPrice).toLocaleString("en-US", { maximumFractionDigits: 2, minimumFractionDigits: 2 }));
        }
    });

    $.ajax({
        type: 'GET',
        url: "/binance_eth",
        success: function (data) {
            var prices = data
            var $bin_buy_eth_price = $('#bin_buy_eth_price');
            var $bin_sell_eth_price = $('#bin_sell_eth_price');

            $bin_buy_eth_price.text("$" + parseFloat(prices.askPrice).toLocaleString("en-US", { maximumFractionDigits: 2, minimumFractionDigits: 2 }));
            $bin_sell_eth_price.text("$" + parseFloat(prices.lastPrice).toLocaleString("en-US", { maximumFractionDigits: 2, minimumFractionDigits: 2 }));
        }
    });

    $.ajax({
        type: 'GET',
        url: "/recommendation",
        success: function (data) {
            var recom = data
            console.log(recom);

            $('#btc_recom').text(recom.btc_recommendation);
            $('#eth_recom').text(recom.eth_recommendation);
        }
    });


});