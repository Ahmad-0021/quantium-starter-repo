from app import app


def test_header_present(dash_duo):
    """Verify the application header is rendered."""
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#app-header', timeout=10)
    header = dash_duo.find_element('#app-header')
    assert 'Pink Morsel' in header.text


def test_visualisation_present(dash_duo):
    """Verify the sales line chart visualisation is rendered."""
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#sales-line-chart', timeout=10)
    assert dash_duo.find_element('#sales-line-chart') is not None


def test_region_picker_present(dash_duo):
    """Verify the region filter radio buttons are rendered."""
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#region-filter', timeout=10)
    assert dash_duo.find_element('#region-filter') is not None
