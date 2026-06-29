import sys


def main():
    print("=== Player Score Analytics ===")

    scores = sys.argv[1:]
    score_list = []

    for i in scores:
        try:
            score = int(i)
            score_list.append(score)
        except ValueError:
            print(f"Invalid parameter: `{i}`")
            return

    if len(score_list) == 0:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return

    total_players = len(score_list)
    total_score = sum(score_list)
    average_score = total_score / total_players
    high_score = max(score_list)
    low_score = min(score_list)
    score_range = high_score - low_score

    print(f"Scores processed: {score_list}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score rangte: {score_range}")


if __name__ == "__main__":
    main()
