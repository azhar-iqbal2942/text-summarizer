from typing import List


class Summary:
    summarizer_text_divisor_mappings = {
        60: 3,
        80: 4,
        90: 5,
    }

    def get_text_summary(self, text: str, summary_length: int):
        parsed_content = self._parse_text(text)
        text_display_size = self._get_summary_length_size(
            summary_length, len(parsed_content)
        )
        intial_part = parsed_content[:text_display_size]
        middle_part = parsed_content[len(parsed_content) // 2]
        ending_part = parsed_content[
            -(text_display_size - 1 if text_display_size > 1 else 1) :
        ]
        final = ".".join(intial_part + [middle_part] + ending_part)

        return final

    def _parse_text(self, text: str) -> List[str]:
        return text.split(".")

    def _get_summary_length_size(self, summary_length: int, text_length: int):
        if summary_length >= 20 and summary_length <= 60:
            return self._calculate_text_size_to_display(
                mapping_value=60, text_length=text_length
            )
        elif summary_length > 60 and summary_length <= 80:
            return self._calculate_text_size_to_display(
                mapping_value=80, text_length=text_length
            )
        else:
            return self._calculate_text_size_to_display(
                mapping_value=90, text_length=text_length
            )

    def _calculate_text_size_to_display(self, mapping_value: int, text_length: int):
        divisor = self.summarizer_text_divisor_mappings[mapping_value]
        text_display_size = text_length // divisor
        return text_display_size
