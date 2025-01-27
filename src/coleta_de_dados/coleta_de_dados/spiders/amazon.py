import scrapy
from datetime import datetime


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com.br/s?k=headset+gamer']
    first_page = 1
    end_page = 10

    def parse(self, response):
        products = response.css(
            '.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small'
        )
        for product in products:
            yield {
                'product_name': product.css(
                    '.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal span::text'
                ).get(),
                'reviews': product.css(
                    '.a-section.a-spacing-none.a-spacing-top-micro .a-row.a-size-small .a-icon-alt::text'
                ).get(),
                'reviews_qtd': product.css(
                    '.a-size-base.s-underline-text::text'
                ).get(),
                'product_price_local': product.css(
                    '.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal .a-price .a-price-symbol::text'
                ).get(),
                'product_price': product.css(
                    '.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal .a-price .a-price-whole::text'
                ).get(),
                'product_price_fraction': product.css(
                    '.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal .a-price .a-price-fraction::text'
                ).get(),
                'modified_date': datetime.now().strftime('%y/%m/%d %H:%M:%S'),
            }
        if self.first_page < self.end_page:
            next_page = response.css(
                'li.s-list-item-margin-right-adjustment a::attr("href")'
            ).get()
            if next_page is not None:
                self.first_page += 1
                yield response.follow(next_page, self.parse)


# fetch('https://www.amazon.com/s?k=gaming+headsets&language=pt_BR&currency=BRL')
# response.css('div.puisg-col-inner')
# len(response.css('div.puisg-col-inner'))

# products.css('.a-link-normal.s-line-clamp-2.s-link-style.a-text-normal')
# products.css('.a-size-medium.a-spacing-none.a-color-base.a-text-normal span::text').get()
# products.css('.a-icon.a-icon-star-small.a-star-small-4 span::text').get()
# products.css('.a-size-base.s-underline-text::text').get()
# products.css('.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal .a-price .a-price-symbol::text').get()
# products.css('.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal .a-price .a-price-whole::text').get()
# products.css('.a-link-normal.s-no-hover.s-underline-text.s-underline-link-text.s-link-style.a-text-normal .a-price .a-price-fraction::text').get()

# a-offscreen
# a-size-base.s-underline-text
# a-icon.a-icon-star-small.a-star-small-4


# products.css('.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal')
