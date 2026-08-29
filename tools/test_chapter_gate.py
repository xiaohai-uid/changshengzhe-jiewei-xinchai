#!/usr/bin/env python3
import unittest

import chapter_gate as gate


class ChapterGateTests(unittest.TestCase):
    def test_detects_short_paragraph_waterfall(self):
        text = "第一句。\n\n第二句。\n\n第三句。\n\n第四段有两句。这里继续。"
        self.assertEqual(gate.max_consecutive_one_sentence_narrative(gate.paragraphs(text)), 3)

    def test_dialogue_does_not_count_as_narrative_waterfall(self):
        text = "“一句。”\n\n“第二句。”\n\n“第三句。”\n\n叙述有两句。这里继续。"
        self.assertEqual(gate.max_consecutive_one_sentence_narrative(gate.paragraphs(text)), 0)

    def test_rule_matrix_extracts_rule_ids(self):
        text = "| WF-001 | a |\n| STYLE-003 | b |\n| PAY-004 | c |"
        self.assertEqual(gate.rule_ids_from_matrix(text), {"WF-001", "STYLE-003", "PAY-004"})

    def test_coverage_extracts_status(self):
        text = "| WF-001 | PASS | evidence |\n| PAY-004 | NA | no power use |"
        self.assertEqual(gate.coverage_from_audit(text), {"WF-001": "PASS", "PAY-004": "NA"})

    def test_candidate_hash_changes_on_edit(self):
        self.assertNotEqual(gate.sha256_text("甲"), gate.sha256_text("乙"))

    def test_backend_patterns_detect_repository_language(self):
        text = "本章里出现了CH007和Canon。"
        hit_names = {name for name, pattern in gate.BACKEND_PATTERNS.items() if pattern.search(text)}
        self.assertIn("chapter_id", hit_names)
        self.assertIn("canon", hit_names)
        self.assertIn("author_chapter_ref", hit_names)


if __name__ == "__main__":
    unittest.main()
