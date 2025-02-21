from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}  # DSU parent mapping
        email_to_name = {}  # Email -> Name mapping

        # Find function with path compression
        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]

        # Union function to merge sets
        def union(email1, email2):
            root1, root2 = find(email1), find(email2)
            if root1 != root2:
                parent[root2] = root1  # Merge sets

        # Step 1: Initialize DSU for emails and map emails to names
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email  # Self parent
                email_to_name[email] = name  # Store name
                union(first_email, email)  # Union emails

        # Step 2: Group emails by their root parent
        merged_accounts = defaultdict(set)
        for email in parent:
            root = find(email)  # Find ultimate parent
            merged_accounts[root].add(email)

        # Step 3: Format output by sorting emails and adding names
        result = []
        for root_email, emails in merged_accounts.items():
            result.append([email_to_name[root_email]] + sorted(emails))

        return result
