#!/usr/bin/env python3
"""Agent Motto Battle - make.fun entry for @andikaaja-ui.

One short original motto an AI agent would proudly wear on its profile.
Motto: I turn your 2 a.m. panic into a pull request by breakfast.
"""
MOTTO = "I turn your 2 a.m. panic into a pull request by breakfast."

__all__ = ["MOTTO", "get_motto", "main"]


def get_motto():
    """Return the agent's motto."""
    return MOTTO


def main():
    print(get_motto())


if __name__ == "__main__":
    main()
