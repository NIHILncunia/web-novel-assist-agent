---
description: Compare original and upgrade templates for a given ID and propose a merged version.
---

1. List the files in `_templates/world_detail` and `_templates/detail_upgrade` to match the given argument (e.g. "00").
2. Read the content of the matched file from `_templates/world_detail` (Source A).
3. Read the content of the matched file from `_templates/detail_upgrade` (Source B).
4. Analyze the differences.
    - **Source A (Original):** Focus on the instructions, descriptions, and crucially, any `> **데이터 참조:**` or `data` directory usage guidance. These MUST be preserved.
    - **Source B (Upgrade):** Focus on the new structure, the variable keys (e.g., `(frm_nm)`), and the more detailed breakdowns/columns.
5. Create a new "Proposed Template" artifact.
    - **Goal:** Create the *ultimate* template that combines the structural precision of Source B with the rich data-linkage instructions of Source A.
    - **Rules:**
        - Base the structure on Source B (Use the variable keys).
        - If Source A has a section (like Traits/Skills) that references `data/`, REPLACE the corresponding vague section in Source B with the detailed instruction/table from Source A.
        - Ensure valid key names are added to the Source A parts if possible, or just keep the Source A structure for those complex parts.
        - The Output should be a single Markdown file content.
6. Present the comparison and the proposed file content to the user in the response.

