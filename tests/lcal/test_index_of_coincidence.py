import lcal.frequency_analysis as fa
import lcal.index_of_coincidence as ioc

def test_from_text():
    assert abs(ioc.from_text("Hello World! (WOW)") - 0.05833) < 0.01
    assert abs(ioc.from_text("Hello World! (WOW)", target_pattern="[a-zA-Z]*") - 0.08974) < 0.01
    assert abs(ioc.from_text("Hello World! (WOW)", target_pattern="[A-Z]*", normalize=True) - 0.11538) < 0.01
