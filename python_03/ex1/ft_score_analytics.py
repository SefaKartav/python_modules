import sys


def main():
    args = sys.argv[1:]

    scores = []

    for i in args:
        try:
            score = int(i)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: {i}")

    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...\n")
        return

    Total_players = len(scores)
    Total_score = sum(scores)
    Average_score = Total_score / Total_players
    High_score = max(scores)
    Low_score = min(scores)
    Score_range = High_score - Low_score

    print(f"Total players: {Total_players}")
    print(f"Total score: {Total_score}")
    print(f"Average score: {Average_score}")
    print(f"High score: {High_score}")
    print(f"Low score: {Low_score}")
    print(f"Score range: {Score_range}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    main()
