import matplotlib.pyplot as plt

def visualize_all(spf_list, update_functions, lower_quota_values, gini_values, avg_footrule_values, avg_kt_values, std_kt_values, egalitarian_kt_values, lower_quota_ratios_special_voter, avg_sq_kt_values):
    draw_perpetual_lower_quota_compliance_all(lower_quota_values, spf_list, update_functions, "equal", 0, "plots/lower_quota_plot_1.png")
    draw_perpetual_lower_quota_compliance_all(lower_quota_values, spf_list, update_functions, "equal", 3, "plots/lower_quota_plot_2.png")
    draw_perpetual_lower_quota_compliance_all(lower_quota_values, spf_list, update_functions, "equal", 7, "plots/lower_quota_plot_3.png")

    draw_perpetual_lower_quota_compliance_all(lower_quota_values, spf_list, update_functions, "special-voter-25-percent", 0, "plots/lower_quota_plot_1_25.png")
    draw_perpetual_lower_quota_compliance_all(lower_quota_values, spf_list, update_functions, "special-voter-25-percent", 3, "plots/lower_quota_plot_2_25.png")
    draw_perpetual_lower_quota_compliance_all(lower_quota_values, spf_list, update_functions, "special-voter-25-percent", 7, "plots/lower_quota_plot_3_25.png")

    draw_gini_all(gini_values, spf_list, update_functions, "equal", 0, "plots/gini_plot_1.png")    
    draw_gini_all(gini_values, spf_list, update_functions, "equal", 3, "plots/gini_plot_2.png")
    draw_gini_all(gini_values, spf_list, update_functions, "equal", 7, "plots/gini_plot_3.png")

    draw_gini_all(gini_values, spf_list, update_functions, "special-voter-25-percent", 0, "plots/gini_plot_1_25.png")    
    draw_gini_all(gini_values, spf_list, update_functions, "special-voter-25-percent", 3, "plots/gini_plot_2_25.png")
    draw_gini_all(gini_values, spf_list, update_functions, "special-voter-25-percent", 7, "plots/gini_plot_3_25.png")

    draw_spearman_footrule_all(avg_footrule_values, spf_list, update_functions, "equal", 0, "plots/footrule_plot_1.png")
    draw_spearman_footrule_all(avg_footrule_values, spf_list, update_functions, "equal", 3, "plots/footrule_plot_2.png")
    draw_spearman_footrule_all(avg_footrule_values, spf_list, update_functions, "equal", 7, "plots/footrule_plot_3.png") 

    draw_spearman_footrule_all(avg_footrule_values, spf_list, update_functions, "special-voter-25-percent", 0, "plots/footrule_plot_1_25.png")
    draw_spearman_footrule_all(avg_footrule_values, spf_list, update_functions, "special-voter-25-percent", 3, "plots/footrule_plot_2_25.png")
    draw_spearman_footrule_all(avg_footrule_values, spf_list, update_functions, "special-voter-25-percent", 7, "plots/footrule_plot_3_25.png") 

    draw_average_kt_all(avg_kt_values, spf_list, update_functions, "equal", 0, "plots/avg_kt_plot_1.png")
    draw_average_kt_all(avg_kt_values, spf_list, update_functions, "equal", 3, "plots/avg_kt_plot_2.png")
    draw_average_kt_all(avg_kt_values, spf_list, update_functions, "equal", 7, "plots/avg_kt_plot_3.png")

    draw_average_kt_all(avg_kt_values, spf_list, update_functions, "special-voter-25-percent", 0, "plots/avg_kt_plot_1_25.png")
    draw_average_kt_all(avg_kt_values, spf_list, update_functions, "special-voter-25-percent", 3, "plots/avg_kt_plot_2_25.png")
    draw_average_kt_all(avg_kt_values, spf_list, update_functions, "special-voter-25-percent", 7, "plots/avg_kt_plot_3_25.png")

    draw_standard_deviation_kt_all(std_kt_values, spf_list, update_functions, "equal", 0, "plots/std_kt_plot_1.png")
    draw_standard_deviation_kt_all(std_kt_values, spf_list, update_functions, "equal", 3, "plots/std_kt_plot_2.png")
    draw_standard_deviation_kt_all(std_kt_values, spf_list, update_functions, "equal", 7, "plots/std_kt_plot_3.png")

    draw_standard_deviation_kt_all(std_kt_values, spf_list, update_functions, "special-voter-25-percent", 0, "plots/std_kt_plot_1_25.png")
    draw_standard_deviation_kt_all(std_kt_values, spf_list, update_functions, "special-voter-25-percent", 3, "plots/std_kt_plot_2_25.png")
    draw_standard_deviation_kt_all(std_kt_values, spf_list, update_functions, "special-voter-25-percent", 7, "plots/std_kt_plot_3_25.png")

    draw_egalitarian_kt_all(egalitarian_kt_values, spf_list, update_functions, "equal", 0, "plots/egalitarian_kt_plot_1.png")
    draw_egalitarian_kt_all(egalitarian_kt_values, spf_list, update_functions, "equal", 3, "plots/egalitarian_kt_plot_2.png")
    draw_egalitarian_kt_all(egalitarian_kt_values, spf_list, update_functions, "equal", 7, "plots/egalitarian_kt_plot_3.png")

    draw_egalitarian_kt_all(egalitarian_kt_values, spf_list, update_functions, "special-voter-25-percent", 0, "plots/egalitarian_kt_plot_1_25.png")
    draw_egalitarian_kt_all(egalitarian_kt_values, spf_list, update_functions, "special-voter-25-percent", 3, "plots/egalitarian_kt_plot_2_25.png")
    draw_egalitarian_kt_all(egalitarian_kt_values, spf_list, update_functions, "special-voter-25-percent", 7, "plots/egalitarian_kt_plot_3_25.png")
    
    draw_perpetual_lower_quota_ratio_all(lower_quota_ratios_special_voter, spf_list, update_functions, "equal", 0, "plots/perpetual_lower_quota_ratio_1.png")
    draw_perpetual_lower_quota_ratio_all(lower_quota_ratios_special_voter, spf_list, update_functions, "equal", 3, "plots/perpetual_lower_quota_ratio_2.png")
    draw_perpetual_lower_quota_ratio_all(lower_quota_ratios_special_voter, spf_list, update_functions, "equal", 7, "plots/perpetual_lower_quota_ratio_3.png")

    draw_perpetual_lower_quota_ratio_all(lower_quota_ratios_special_voter, spf_list, update_functions, "special-voter-25-percent", 0, "plots/perpetual_lower_quota_ratio_1_25.png")
    draw_perpetual_lower_quota_ratio_all(lower_quota_ratios_special_voter, spf_list, update_functions, "special-voter-25-percent", 3, "plots/perpetual_lower_quota_ratio_2_25.png")
    draw_perpetual_lower_quota_ratio_all(lower_quota_ratios_special_voter, spf_list, update_functions, "special-voter-25-percent", 7, "plots/perpetual_lower_quota_ratio_3_25.png")

    draw_average_sq_kt_all(avg_sq_kt_values, spf_list, update_functions, "equal", 0, "plots/avg_sq_kt_plot_1.png")
    draw_average_sq_kt_all(avg_sq_kt_values, spf_list, update_functions, "equal", 3, "plots/avg_sq_kt_plot_2.png")
    draw_average_sq_kt_all(avg_sq_kt_values, spf_list, update_functions, "equal", 7, "plots/avg_sq_kt_plot_3.png")

    draw_average_sq_kt_all(avg_sq_kt_values, spf_list, update_functions, "special-voter-25-percent", 0, "plots/avg_sq_kt_plot_1_25.png")
    draw_average_sq_kt_all(avg_sq_kt_values, spf_list, update_functions, "special-voter-25-percent", 3, "plots/avg_sq_kt_plot_2_25.png")
    draw_average_sq_kt_all(avg_sq_kt_values, spf_list, update_functions, "special-voter-25-percent", 7, "plots/avg_sq_kt_plot_3_25.png")


def draw_metric_all(metric_values, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name, metric_name="Metric Value"):
    """
    Plots a generic metric for all update functions and SPFs for a given initialization and threshold.
    
    :param metric_values: list of (spf, update_func, init, threshold, metric)
    :param spf_list: list of SPFs
    :param update_functions: list of update functions
    :param init_to_plot: given weight initialization (e.g., "equal")
    :param threshold_to_plot: given satisfaction threshold (e.g., 3)
    :param file_name: Name of the file to save the plot 
    :param metric_name: Name of the metric to be plotted (default: "Metric Value")
    """
    # Organize data for plotting
    plot_data = {spf: [] for spf in spf_list}
    for spf in spf_list:
        for update_func in update_functions:
            # Find the metric value for this (spf, update_func, init, threshold)
            value = None
            for (s, u, init, threshold, metric) in metric_values:
                if s == spf and u == update_func and init == init_to_plot and threshold == threshold_to_plot:
                    value = metric
                    break
            plot_data[spf].append(value)
    
    # Plot
    plt.figure(figsize=(10, 6))
    for spf in spf_list:
        plt.scatter(update_functions, plot_data[spf], marker='o', label=spf)
    plt.title(f"{metric_name} (init={init_to_plot}, threshold={threshold_to_plot})")
    plt.xlabel("Update Function")
    plt.ylabel(metric_name)
    plt.xticks(rotation=45)
    plt.legend(title='SPF')
    plt.tight_layout()
    plt.savefig(file_name)
    plt.close()

 
def draw_gini_all(gini_values, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name):
    """
    Plots Gini influence coefficient for all update functions and SPFs for a given initialization and threshold.
    
    :param gini_values: list of (spf, update_func, init, threshold, gini)
    :param spf_list: list of SPFs
    :param update_functions: list of update functions
    :param init_to_plot: given weight initialization (e.g., 'equal')
    :param threshold_to_plot: given satisfaction threshold (e.g., 3)
    :param file_name: Name of the file to save the plot 
    """
    draw_metric_all(
        gini_values, spf_list, update_functions, init_to_plot, threshold_to_plot, 
        file_name, metric_name="Gini Influence Coefficient"
    )

def draw_perpetual_lower_quota_compliance_all(lower_quota_values, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name):
    draw_metric_all(
        lower_quota_values, spf_list, update_functions, init_to_plot, threshold_to_plot,
        file_name, metric_name="Perpetual Lower Quota Compliance"
    )

def draw_spearman_footrule_all(avg_footrule_values, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name):
    draw_metric_all(
        avg_footrule_values, spf_list, update_functions, init_to_plot, threshold_to_plot,
        file_name, metric_name="Average Spearman Footrule Distance"
    )

def draw_average_kt_all(avg_kt_values, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name):
    draw_metric_all(
        avg_kt_values, spf_list, update_functions, init_to_plot, threshold_to_plot,
        file_name, metric_name="Average KT Distance"
    )
    
def draw_standard_deviation_kt_all(std_kt_values, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name):
    draw_metric_all(
        std_kt_values, spf_list, update_functions, init_to_plot, threshold_to_plot,
        file_name, metric_name="Standard Deviation of KT Distance"
    )
    
def draw_egalitarian_kt_all(egalitarian_kt_values, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name):
    draw_metric_all(
        egalitarian_kt_values, spf_list, update_functions, init_to_plot, threshold_to_plot,
        file_name, metric_name="Egalitarian KT Distance"
    )

def draw_perpetual_lower_quota_ratio_all(lower_quota_ratios_special_voter, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name):
    draw_metric_all(
        lower_quota_ratios_special_voter, spf_list, update_functions, init_to_plot, threshold_to_plot,
        file_name, metric_name="Perpetual Lower Quota Ratio Special Voter"
    )

def draw_average_sq_kt_all(avg_sq_kt_values, spf_list, update_functions, init_to_plot, threshold_to_plot, file_name):
    draw_metric_all(
        avg_sq_kt_values, spf_list, update_functions, init_to_plot, threshold_to_plot,
        file_name, metric_name="Average Squared KT Distance"
    )