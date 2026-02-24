from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = chromium_page_with_state.get_by_test_id('courses-drawer-list-item-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        empty_block_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_block_icon).to_be_visible()

        no_results_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_block).to_be_visible()
        expect(no_results_block).to_have_text('There is no results')

        results_here_message = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(results_here_message).to_be_visible()
        expect(results_here_message).to_have_text('Results from the load test pipeline will be displayed here')